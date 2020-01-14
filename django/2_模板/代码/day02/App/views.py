from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import User


def home(request,cid=0):
    return HttpResponse("首页--"+str(cid))


def show(request,name):
    return HttpResponse("show:"+name)


def add(request,num):
    return HttpResponse(str(num))


def sub(request,num):
    return HttpResponse("slug:  "+num)


def enter(request,path):
    return HttpResponse(path)


def list_qq(request,qq):
    return HttpResponse(qq)


def get_user(request):
    data = User.objects.all()[:10]
    # 将Querset转换为列表
    data = list(data.values())
    return JsonResponse(data,safe=False)


def my_redirect(request):
    # 无参路由，硬编码,直接写请求路径
    # return redirect("/")
    # return redirect("/json/")
    name = 'admin'
    # 带参数
    # return  redirect(f"/show/{name}/"))


    # return  redirect("/show/{name}/".format(name=name))
    # 带反向解析的重定向
    # print(reverse("App:home"))
    # return  redirect(reverse("App:home"))

    # 带参数的反向解析
    # print(reverse("App:add",kwargs={'num':90}))
    # 位置参数
    # return redirect(reverse("App:add",args=(30,)))
    # 关键字参数
    # return redirect(reverse("App:add",kwargs={'num':100}))

    # 反向解析在模板中用法
    return render(request,"redirect.html",context={'num':100})