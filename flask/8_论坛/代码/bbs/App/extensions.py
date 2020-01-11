# -*- coding: utf-8 -*-
# @File    : extensions.py
# 描述     ：应用扩展模块：加载各种类的实例，数据库、邮件、bootstap
# @Time    : 2020/1/7 14:15
# @Author  : 
# @QQ      :  

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

# 初始化
def init_app(app):
    db.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)

    # 设置登录端点
    login_manager.login_view = 'user.login' # 蓝图名.视图函数名