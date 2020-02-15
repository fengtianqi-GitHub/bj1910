#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: middlewares.py
@time: 2020/2/14 11:09 上午
'''


from django.utils.deprecation import MiddlewareMixin


# 自定义中间件类必须继承MiddlewareMixin
class MiddleWare1(MiddlewareMixin):
    def process_request(self,request):
        print("request")
        # 一般不需要返回值

    def process_view(self,request,view_func,view_args,view_kwargs):
        """
        先于自己视图函数处理
        :param request: 请求对象
        :param view_func: 将要调用的视图函数地址
        :param view_args: 位置参数
        :param view_kwargs: 关键字参数
        :return:
        """
        print("view")

    def process_response(self,request,response):
        print("response")
        return response

