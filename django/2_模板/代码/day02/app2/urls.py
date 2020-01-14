# -*- coding: utf-8 -*-
# @File    : urls.py
# 描述     ：
# @Time    : 2020/1/14 11:22
# @Author  : 
# @QQ      :  

from django.urls import path, include

from app2 import views
app_name = 'app2'
urlpatterns = [
    path('template/',views.load_template,name='load_template'),
    path("var/",views.show_var,name='var'),
    path("filter/",views.use_filter,name='filter'),
    path("inner/",views.define_inner,name='inner'),
    path("login/",views.login,name='login'),
    path("ext/",views.extend,name='extend'),
]
