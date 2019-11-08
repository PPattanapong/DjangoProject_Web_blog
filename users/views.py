from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #6 import forms เริ่มต้น UserCreationForm มี 'user' 'password1' 'password2'
from .forms import UserRegisterForm #6 import forms สร้างใหม่ UserCreationForm มี 'user' 'email' 'password1' 'password2'
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): # 6
            form.save() # บันทึกค่าลงใน ฐานขู้อมูล
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login {username}!')   # แสดงข้อความว่า ... ตามด้วยชื่อ user ที่สมัคร
            return redirect('login')  # ไปผยังหน่า 'stme-home'
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})    #ไม่ส่งค่า กลับมาหน้า register



@login_required #7 ฟังชั่นช่วย login ก่อนถึงจะเห็นโปรไฟล์ได้
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form,
        }

        return render(request, 'users/profile.html', context)
