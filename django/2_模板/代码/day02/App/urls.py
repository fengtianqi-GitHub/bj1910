# -*- coding: utf-8 -*-
# @File    : urls.py
# 描述     ：
# @Time    : 2020/1/14 9:14
# @Author  : 
# @QQ      :  

from django.urls import path, re_path
from . import views
app_name = 'App'
urlpatterns = [
    # 可以多个路由匹配同一个视图函数
    path("",views.home,name='home'),
    path("<int:cid>/",views.home,name='home'),

    path("show/<name>/",views.show,name='show'),
    path("add/<int:num>/",views.add,name='add'),
    path("sub/<slug:num>/",views.sub,name='sub'),
    path("enter/<path:path>/",views.enter,name='enter'),

    #re_path 正则匹配
    re_path(r'^list/([1-9]\d{4,10})/$',views.list_qq,name='list'),

    # JsonResponse
    path("json/",views.get_user,name='json'),

    # 重定向
    path("redirect/",views.my_redirect,name='redirect'),
]
