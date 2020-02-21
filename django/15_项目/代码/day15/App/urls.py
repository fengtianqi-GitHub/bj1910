#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    路由配置
@author:  
@contact: 
@file: urls.py
@time: 2020/2/21 9:25 上午
'''
from django.urls import path

from App import views

app_name = 'App'
urlpatterns = [
    path('book/',views.BooksView.as_view(),name='book'),
    # path('list/',views.ListView.as_view(),name='list'),
    path('list/<int:pk>', views.ListView.as_view(),name='list'),
]