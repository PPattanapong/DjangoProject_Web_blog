from django.shortcuts import render, get_object_or_404, redirect      #3
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponse      #2
from .models import Post
from .forms import CommentForm
from .models import Post, Comment
from taggit.models import Tag

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'stme/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'stme/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5        #กำหนดจำนวนโพสที่แสดง

    def get_queryset(self):
        queryset = super().get_queryset().filter()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['queryset'] = self.get_queryset()
        return context

class UserPostListView(ListView):
    model = Post
    template_name = 'stme/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5         #กำหนดจำนวนโพสที่แสดง

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView): #10 #LoginRequiredMixin กำหนดให้ ต้อง login ก่อน
    model = Post
    fields = ['title', 'content', 'tags',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #10 #LoginRequiredMixin กำหนดให้ ต้อง login ก่อน
    model = Post
    fields = ['title', 'content','tags']

    def form_valid(self, form): # save to db
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #10 ฟังค์ชั่นปล้องกันการแก้ไขโพาของคนอื่น
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'  #กลับไปหน้าแรก และ ลบโพส
    def test_func(self): #10 ฟังค์ชั่นปล้องกันการแก้ไขโพาของคนอื่น
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def djangoSTMe(request): #สร้างการเชื่อมต่อกับไฟล์ about
    return render(request, 'stme/django.html', {'title': 'Django'})

def about(request): #สร้างการเชื่อมต่อกับไฟล์ about
    return render(request, 'stme/about.html', {'title': 'About'})



@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'stme/add_comment_to_post.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post-detail', pk=comment.post.pk)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'stme/home.html', context)