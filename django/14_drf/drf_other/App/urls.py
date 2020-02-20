#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: urls.py
@time: 2020/2/20 9:51 上午
'''
from django.urls import path

from App import views
app_name = "App"
urlpatterns = [
    path("book/",views.BooksView.as_view(),name='book'),
    path("book/<int:bid>/",views.BooksView.as_view(),name='book'),
    path("index/",views.IndexView.as_view(),name='index'),

    # 用户注册
    path('register/',views.UserRegisterView.as_view(),name='register'),

]