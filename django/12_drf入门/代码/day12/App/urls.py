#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: urls.py
@time: 2020/2/18 11:36 上午
'''
from django.urls import path

from App import views

app_name = 'App'
urlpatterns = [
    path('list/', views.list_user, name='list'),
]