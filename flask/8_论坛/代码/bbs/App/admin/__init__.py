# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# 描述     ：
# @Time    : 2020/1/7 14:48
# @Author  : 
# @QQ      :  

from .category import cat

def dog_blueprint(app):
    app.register_blueprint(cat)