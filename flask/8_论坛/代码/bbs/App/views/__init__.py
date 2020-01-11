# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# 描述     ：
# @Time    : 2020/1/7 14:49
# @Author  : 
# @QQ      :  
from .user import user
from .views import bbs

# 注册蓝图
def register_blueprint(app):
    app.register_blueprint(user)
    app.register_blueprint(bbs)

