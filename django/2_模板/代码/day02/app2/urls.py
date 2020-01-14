# -*- coding: utf-8 -*-
# @File    : urls.py
# 描述     ：
# @Time    : 2020/1/14 11:22
# @Author  : 
# @QQ      :  

from django.urls import path, include

from app2 import views

urlpatterns = [
    path('template/',views.load_template,name='load_template')
]
