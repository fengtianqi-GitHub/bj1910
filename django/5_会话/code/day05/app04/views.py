from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
            # password会自动签名
            User.objects.create_user(username=username,password=password,email=email)
            # 转到登录界面
            return redirect(reverse("app04:login"))
    else:
        return render(request,'app04/register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        # 验证是否是合法用户
        # 如果用户名和密码都正确，返回用户对象，否则返回None
        user = authenticate(request,username=username,password=password)
        print(user,type(user))
        if user: # 用户存在
            # 把用户信息写入session
            # 第二个参数是用户对象
            login(request,user)
            return redirect(reverse("app04:index"))
        else:
            return redirect(reverse("app04:login"))
    return render(request,"app04/login.html")


def index(request):
    return render(request,'app04/index.html')


def user_logout(request):
    # 退出登录
    logout(request)
    return redirect(reverse("app04:index"))

# 路由保护，参数login_url表示如果未登录需要跳转的页面地址
@login_required(login_url='/app04/login/')
def get_money(request):
    return HttpResponse("a lot of money")