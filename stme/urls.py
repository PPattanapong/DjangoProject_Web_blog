from django.urls import path
from django.conf.urls import url
from .views import (
    PostListView,
    PostDetailView, #10
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,

)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='stme-home'), # ประกาศ URL จาก ไฟล์ views ฟังชั้น home ตั้ง name url เป็น 'stme-home' #2
    path('django/', views.djangoSTMe, name='stme-django'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'), # <int:pk> กำหนดดให้ ID เจ้าของ Post สามารถแก้ไขได้
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), # <int:pk> เข้าไปที่ ID
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='stme-about'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),


]