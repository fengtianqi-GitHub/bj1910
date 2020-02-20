#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: MyPaginations.py
@time: 2020/2/20 4:41 下午
'''
from rest_framework.pagination import PageNumberPagination
# page_size每页显示的记录个数
# page 是第几页
# http://127.0.0.1:8013/book/?page=2&page_size=3

class MyPagination(PageNumberPagination):
    page_size = 3  # 每页记录个数
    page_size_query_param = 'page_size'
    page_query_param = 'page'  # 分页参数名