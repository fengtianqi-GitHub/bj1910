#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    过滤
@author:  
@contact: 
@file: filters.py
@time: 2020/2/21 9:58 上午
'''
import django_filters
from django_filters import rest_framework as filters

from App.models import Bookinfo


class BookFilter(django_filters.FilterSet):
    class Meta:
        # http://127.0.0.1:8000/book/?min_read=10&max_read=50
        # field_name="bread" 模型中的字段名;lookup_expr是运算，gte表示>=
        min_read = filters.NumberFilter(field_name="bread", lookup_expr='gte')
        max_read = filters.NumberFilter(field_name="bread", lookup_expr='lte')
        model = Bookinfo  # 模型
        fields = {
            'btitle':['icontains'],  # 键是字段名,列表里是查询进行运算
             # http://127.0.0.1:8000/book/?bcomment__gte=30&bcomment__lte=60
            'bcomment':['gte','lte'],
        }