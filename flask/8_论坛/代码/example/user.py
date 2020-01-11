# -*- coding: utf-8 -*-
# @File    : user.py
# 描述     ：
# @Time    : 2020/1/9 15:39
# @Author  : 
# @QQ      :  
from flask import Blueprint, make_response, session

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/login/')
def login():
    response = make_response()
    from datetime import timedelta,datetime
    future = datetime.now() + timedelta(days=3)
    response.set_cookie('password','123',expires=future)
    return response
@user.route("/register/")
def register():
    session['name'] = 'admin'
    return "register"