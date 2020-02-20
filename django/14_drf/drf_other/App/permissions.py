#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    权限
@author:  
@contact: 
@file: permissions.py
@time: 2020/2/20 3:22 下午
'''
from rest_framework.permissions import BasePermission

from App.models import User


class BookPermission(BasePermission):
    # 针对视图
    def has_permission(self, request, view):
        print("hahahah")
        # 返回True就是有权限，False就是没有权限
        # 登录用户有操作权限
        return isinstance(request.user,User)

    # 针对对象的
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        else:
            return False

