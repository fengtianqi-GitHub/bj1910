# -*- coding: utf-8 -*-
# @File    : forms.py
# 描述     ：
# @Time    : 2020/1/14 17:47
# @Author  : 
# @QQ      :  

from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(max_length=60,min_length=3,required=True,error_messages={
        'max_length':'用户名最大长度为60',
        'min_length':'用户名最少3个字符',
        'required':'用户名不能为空'
    })
    password = forms.CharField(min_length=3,required=True,error_messages={
        'min_length': '密码最少3个字符',
        'required': '密码不能为空'
    })
    capta = CaptchaField(required=True,error_messages={
        'required':'验证码不能为空',
        'invalid':'验证码不正确'
    })