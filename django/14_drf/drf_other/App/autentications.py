#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    自定义认证类
@author:  csl
@contact: 
@file: autentications.py
@time: 2020/2/20 11:12 上午
'''
from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication
# 在前后端分离的应用中，没有cookie、session
# token 客户登录后，服务器发给客户端的凭证（唯一的字符串）,以后客户端访问服务器
# 需要验证的时候应该带上凭证
from rest_framework.exceptions import AuthenticationFailed

from App.models import User


class MyAuthentication(BaseAuthentication):

    def authenticate(self, request):
        """自定义认证方法"""
        # get请求不需要认证
        # if request.method == "GET":
            # return None

        # 从客户端的查询参数（get参数)获取token
        token = request.query_params.get('token')
        if not token:
            raise AuthenticationFailed("没有token")
        # 从缓存中获取用户uid
        uid = cache.get(token)
        print(uid)
        if not uid:
            raise AuthenticationFailed("token过期了")

        # 从数据库中获取user
        user = User.objects.get(pk=int(uid))
        if not user:
            raise AuthenticationFailed("非法用户")
        print("---------------")
        # 验证通过
        return user,None
