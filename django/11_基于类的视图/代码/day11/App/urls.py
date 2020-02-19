#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: urls.py
@time: 2020/2/17 9:41 上午
'''
from django.urls import path

from App import views
app_name = 'App'
urlpatterns = [
    path('',views.IndexView.as_view(template_name="App/index.html"),name='index'),
    # views.类名.as_view()
    path('register/',views.RegisterView.as_view(),name='register'),

    # listview
    path('list/',views.UserListView.as_view(),name='list'),
    path('list/<int:page>/',views.UserListView.as_view(),name='list'),
    # 用户详细信息
    path('detail/<int:uid>/',views.UserDetailView.as_view(),name='detail'),

    # 创建用户
    path('create/',views.UserAddView.as_view(),name='create'),

    # 类视图中使用装饰器
    path('decator/',views.ExampleView.as_view(),name='decator'),
]