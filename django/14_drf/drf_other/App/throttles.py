#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: throttles.py
@time: 2020/2/20 4:24 下午
'''
from rest_framework.throttling import SimpleRateThrottle


class IndexThrottle(SimpleRateThrottle):
    scope = 'index'
    rate = '2/m'
    # 返回一个区分不同用户的标志
    def get_cache_key(self, request, view):
        return self.get_ident(request)