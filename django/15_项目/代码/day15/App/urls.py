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

    # 调用支付宝客户端
    path('pay/',views.AlipayView.as_view(),name='pay'),
    # 回调地址，支付成功后跳转地址
    path('index/',views.IndexView.as_view(),name='index'),
    # 异步回调，返回订单信息
    path("notify/",views.NotifyView.as_view(),name='notify'),

]