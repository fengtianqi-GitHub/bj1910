# -*- coding: utf-8 -*-
# @File    : register_filter.py
# 描述     ：注册过滤器
# @Time    : 2020/1/14 15:03
# @Author  : 
# @QQ      :  

from django import template

# 实例化一个过滤器注册对象
register = template.Library()

@register.filter(name='sub')
def sub(value,other):
    return value - int(other)
