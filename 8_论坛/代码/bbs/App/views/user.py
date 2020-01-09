# -*- coding: utf-8 -*-
# @File    : user.py
# 描述     ：视图层，管理用户的信息，包括用户的信息维护、登录、注册
# @Time    : 2020/1/7 14:12
# @Author  : 
# @QQ      :
from hashlib import md5

from flask import Blueprint, request, redirect, url_for
from flask_login import login_user,logout_user

from App.models import User,db

user = Blueprint('user',__name__,url_prefix='/user')



@user.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password = md5(password.encode('utf8')).hexdigest()
        # print(password)
        user = User.query.filter(User.username==username,User.password_hash==password).first()
        if user:
            # 将用户信息写入session
            login_user(user)
        # 跳转首页
        return redirect(url_for('bbs.index'))
    else:
        # 登录界面展示
        return "登录"

@user.route('/logout/')
def logout():
    # 退出登录
    logout_user()
    return redirect(url_for('bbs.index'))

@user.route('/test')
def add_user():
    # user = User()
    # user.username = '陈新宇'
    # user.password = '123'
    # db.session.add(user)
    # db.session.commit()
    user = User.query.filter(User.username=='陈新宇').first()
    print(user.check_password('1223'))
    return "add a user"