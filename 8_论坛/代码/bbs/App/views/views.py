# -*- coding: utf-8 -*-
# @File    : views.py
# 描述     ：
# @Time    : 2020/1/7 14:33
# @Author  : 
# @QQ      :  

from flask import Blueprint

bbs = Blueprint('bbs',__name__)

@bbs.route('/')
def index():
    return "这就是首页"