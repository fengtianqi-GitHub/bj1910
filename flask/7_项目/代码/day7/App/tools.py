# -*- coding: utf-8 -*-
# @File    : tools.py
# 描述     ：公用模块
# @Time    : 2020/1/7 9:18
# @Author  : 
# @QQ      :  
"""
#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest



"""
import random

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from flask import current_app


class SMS:
    def __init__(self,signature,template_code):
        """
        :param signature: 签名信息
        :param template_code: 模板代码
        """
        self.signature = signature
        self.template_code = template_code
        self.access_key =  current_app.config.get('ACCESS_KEY_ID')
        self.access_secret =  current_app.config.get('ACCESS_KEY_SECRET')
        self.client = AcsClient(self.access_key, self.access_secret, 'cn-hangzhou')

    def send(self,phone,params):
        """
        :param phone: 电话号码
        :param params: 模板参数，{'参数名':value,...}
        :return:
        """
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')  # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers',phone)
        request.add_query_param('SignName', self.signature)
        request.add_query_param('TemplateCode', self.template_code)
        request.add_query_param('TemplateParam',params)

        response = self.client.do_action_with_exception(request)
        return response
# 短信发送对象
sms = SMS('成少雷','SMS_102315005')
# if __name__ == '__main__':
#     sms = SMS('成少雷','SMS_102315005')
#     print(sms.__dict__)
#     value = str(random.randint(10000,100000))
#     res = sms.send('17852365173',{'number':value})
#     print(res)

