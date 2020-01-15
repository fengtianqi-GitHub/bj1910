# -*- coding: utf-8 -*-
# @File    : urls.py
# 描述     ：
# @Time    : 2020/1/15 9:08
# @Author  : 
# @QQ      :  

from django.urls import path, include

from App import views
app_name = 'App'  # 命名空间
urlpatterns = [
    path("",views.home,name='index'),
    path("new/",views.create,name='new'),
    path("create/",views.process,name='create'),
    path("find/",views.find,name='find'),
    path("query/",views.query1,name='query'),
    path("post/",views.list_post,name='post'),
    path("or/",views.logic_or,name='or'),
    path("manager/",views.custom_manager,name='manager')
]
