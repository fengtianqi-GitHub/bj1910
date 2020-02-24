#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: urls.py
@time: 2020/2/19 9:43 上午
'''
from django.urls import path

from App import views
app_name = 'App'
urlpatterns = [
    path('index/<int:bid>/',views.IndexView.as_view(),name='index'),
    path('req/<int:num>/',views.ReqView.as_view(),name='req'),
    path('gen1/',views.BooksView.as_view(),name='gen1'),
    path('gen2/',views.BooksView2.as_view(),name='gen2'),
    # 修改书籍，一般要传递主键过去
    path('gen3/<int:bid>/',views.BooksView3.as_view(),name='gen3'),
    path('gen4/<int:bid>/',views.BooksView4.as_view(),name='gen4'),

    # 列表和检索特定对象
    path('gen5/',views.BooksView5.as_view(),name='gen5'),
    path('gen5/<int:bid>/',views.BooksView5.as_view(),name='gen5'),
]