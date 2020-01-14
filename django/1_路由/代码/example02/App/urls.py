# -*- coding: utf-8 -*-
# @File    : urls.py
# 描述     ：
# @Time    : 2020/1/13 14:40
# @Author  : 
# @QQ      :  

from django.urls import path, re_path
from App import views
app_name = 'App' # 应用的命名空间
urlpatterns = [
    # re_path的匹配字符串是正则表达式
    # re_path(r'^login/$',views.login)
    # 不带参数路由
    path('login/',views.login,name='login'),
    # 带参路由
    # 1 参数是字符串，默认
    path('show/<name>/',views.show,name='show'),
    # 参数可以指定为整型 <int:参数名>
    path('list/<name>/<int:age>/',views.list_user,name='list'),
    # slug 参数只能是字母、数字、下划线和中划线
    path('bit/<slug:name>/',views.bit,name='bit'),
    # path 路径参数 除空字符外匹配所有字符串
    path("go/<path:lu>/",views.go, name='go'),

    # request
    path("req/",views.show_request,name='req'),

    # response
    path("response/",views.show_response,name='response'),

    # re_path 无命名分组，可以获取传参
    re_path("^phone/(13\d{9})/$",views.phone,name='phone'),

    # re_path 命名分组,视图函数中参数必须和组名一致
    re_path("group/(?P<num>\d+)/",views.get_group,name='group'),
]