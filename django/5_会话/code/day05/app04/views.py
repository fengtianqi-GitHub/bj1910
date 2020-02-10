from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# 用户注册
from django.urls import reverse

from app04.models import User


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.filter(username=username).first()
        if user:
            # 用户名存在
            return render(request,'app04/register.html',context={'error':'用户名已存在'})
        else:
            # 注册用户
            User.objects.create_user(username=username,password=password,email=email)
            # 转到登录界面
            return redirect(reverse("app04:login"))
    return render(request,'app04/register.html')


def login(request):
    return HttpResponse("登录")


def index(request):
    return None


def logout(request):
    return None