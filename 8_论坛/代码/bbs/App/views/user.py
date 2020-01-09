# -*- coding: utf-8 -*-
# @File    : user.py
# 描述     ：视图层，管理用户的信息，包括用户的信息维护、登录、注册
# @Time    : 2020/1/7 14:12
# @Author  : 
# @QQ      :  

from flask import Blueprint, request

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/login/')
def login():
    return "登录"