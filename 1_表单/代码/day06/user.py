# -*- coding: utf-8 -*-
# @File    : user.py
# 描述     ：用户相关处理
# @Time    : 2020/1/6 9:52
# @Author  : 
# @QQ      :  

from flask import Blueprint, current_app, render_template, make_response, session
from flask_mail import Message
from tools import VerifyCode
from ext import mail


user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/register')
def user_register():
    return "用户注册"

@user.route('/send')
def send_mail():
    # 邮件消息对象
    message = Message('2019年终总结',recipients=['1601790761@qq.com'],
                      sender=current_app.config['MAIL_USERNAME'])
    # message.body = "哈喽"  # 文本
    message.html = render_template('新年祝福.html',name='孙文佳')  # html邮件

    mail.send(message)
    return "邮件已发送，请查收"



@user.route('/show')
def show_yzm():
    vc = VerifyCode()
    # 生成验证码
    result = vc.generate()
    session['code'] = vc.code
    response = make_response(result)
    response.headers['content-type'] = 'image/png'
    return response