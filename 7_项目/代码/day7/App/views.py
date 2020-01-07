# -*- coding: utf-8 -*-
# @File    : views.py
# 描述     ：
# @Time    : 2020/1/7 9:40
# @Author  : 
# @QQ      :  

from flask import Blueprint

from App.models import User

bbs = Blueprint('bbs',__name__)

@bbs.route('/')
def index():
    data = User.query.filter().limit(10).all()
    for user in data:
        print(user)
    return "首页"