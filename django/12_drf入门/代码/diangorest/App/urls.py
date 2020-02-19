#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: urls.py
@time: 2020/2/18 3:20 下午
'''
from django.urls import path

from App import views
app_name = 'App'
urlpatterns = [
    path('find/<int:bid>',views.BookInfoView.as_view(),name='find'),
    path('list/',views.BooksView.as_view(),name='list'),
]