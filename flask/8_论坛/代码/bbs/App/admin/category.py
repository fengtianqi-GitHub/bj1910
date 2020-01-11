# -*- coding: utf-8 -*-
# @File    : category.py
# 描述     ：板块管理
# @Time    : 2020/1/7 15:06
# @Author  : 
# @QQ      :
from flask import Blueprint

cat = Blueprint('cat',__name__,url_prefix='/admin')

@cat.route('/category')
def index():
    return "板块管理"