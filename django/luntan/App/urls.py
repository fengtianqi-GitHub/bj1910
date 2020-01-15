# -*- coding: utf-8 -*-
# @File    : urls.py
# 描述     ：
# @Time    : 2020/1/13 17:32
# @Author  : 
# @QQ      :
from django.urls import path

from App import main
app_name = "App"
urlpatterns = [
    path('login/', main.login, name='login'),
    path('', main.index,name='index'),
    path('yzm/',main.yzm,name='yzm'),
]
