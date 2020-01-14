from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def login(request):
    return HttpResponse("登录")


def show(request,name):
    print(name,type(name))
    return HttpResponse("show")


def list_user(request,name,age):
    print(name,type(name))
    print(age,type(age))
    return HttpResponse("显示用户列表")


def bit(request,name):
    print(name)
    return HttpResponse("不是在打架，就是在去打架的路上")


def go(request,lu):
    print(lu,type(lu))
    return HttpResponse("no zuo no die")


def phone(request,*args):
    print(args)
    return HttpResponse("电话")


def get_group(request,num):
    print(num)
    return HttpResponse("命名组参数")


def show_request(request):
    # GET请求参数获取
    # print(request.GET)
    # print(request.GET.get('name'))
    # print(request.GET.get('num'))  # 如果一个参数有多个值，getlisth获取
    # POST参数获取
    # print(request.POST.get('name'))  # 单值参数
    # print(request.POST.getlist('num'))  # 多个值的参数获取用getlist
    # 请求路径
    # print(request.path)
    # method 请求方法
    # print(request.method)
    # 用户请求的原生字典
    # print(request.META)
    # for key,value in request.META.items():
    #     print(key,'-----',value)
    # 是否是ajax请求
    print(request.is_ajax())
    # 完整url
    print(request.build_absolute_uri())
    return HttpResponse("请求对象")


def show_response(request):
    res = HttpResponse("这是响应体")
    res['qiangfeng']='千峰'  # 自定义响应头的键值对
    res.content_type = 'text/html'
    return res