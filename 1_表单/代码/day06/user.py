# -*- coding: utf-8 -*-
# @File    : user.py
# 描述     ：用户相关处理
# @Time    : 2020/1/6 9:52
# @Author  : 
# @QQ      :  

from flask import Blueprint

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/register')
def user_register():
    return "用户注册"