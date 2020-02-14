#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    自定义的中间件
@author:  成少雷
@contact: 
@file: middleware.py
@time: 2020/2/14 10:19 上午
'''
from django.http import HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin


# 自定义中间件类必须继承MiddlewareMixin
class CustomMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        # 统计功能，统计有多少人访问
        # 应该使用redis存储ip地址
        # 用session进行保存
        # ips = request.session.get('ips', [])
        # num = request.session.get('num',0)
        # print(f"num={num}")
        # print(ips)
        # print(request.META["REMOTE_ADDR"])
        # if request.META["REMOTE_ADDR"] not in ips:
        #     ips.append(request.META["REMOTE_ADDR"])
        #     num += 1
        #     request.session['num'] = num
        #     request.session['ips'] = ips

        # 黑名单
        # if request.META["REMOTE_ADDR"] in ['127.0.0.1','10.0.31.253']:
        #     return HttpResponse("你是不受欢迎的客户，get out！")

        # 一般不需要返回值
        pass


    def process_view(self,request,view_func,view_args,view_kwargs):
        """
        先于自己视图函数处理
        :param request: 请求对象
        :param view_func: 将要调用的视图函数地址
        :param view_args: 位置参数
        :param view_kwargs: 关键字参数
        :return:
        """
        print(view_func)
        print("process_view")

    def process_response(self,request,response):
        # print("process_respones")
        # print(response.content.decode('utf-8'))
        if isinstance(response,dict):
            return JsonResponse(response)
        return response






