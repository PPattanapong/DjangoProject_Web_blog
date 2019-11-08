from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # เพิ่ม email ลงในฐานข้อมูลที่สร้างไว้
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm): #9 update 'username' กับ 'email'
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name','last_name','email']

class ProfileUpdateForm(forms.ModelForm): #9  update รูปโปรไฟล์
    class Meta:
        model = Profile
        fields = ['image']