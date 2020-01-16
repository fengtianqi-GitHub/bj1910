# -*- coding: utf-8 -*-
# @File    : urls.py
# 描述     ：
# @Time    : 2020/1/16 9:06
# @Author  : 
# @QQ      :  

from django.urls import path

from App import views
app_name = "App"
urlpatterns = [
    path("",views.home,name='home')
]
