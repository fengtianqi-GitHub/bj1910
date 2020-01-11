# -*- coding: utf-8 -*-
# @File    : forms.py
# 描述     ：表单验证
# @Time    : 2020/1/8 9:34
# @Author  : 
# @QQ      :
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError

from models import User


class RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired("用户名必须输入"),Length(min=3,message="用户名不能少于3位")])
    password = PasswordField('密码',validators=[DataRequired('密码必须输入'),Length(min=6,message='密码至少6位')])
    confirm  = PasswordField('确认密码',validators=[DataRequired('密码必须输入'),EqualTo('password',message="两次密码输入不一致")])

    # 自定义验证用户不能重复
    def validate_username(self,field):
        # field.data是要验证的值
        # print(field,field.data)
        if User.query.filter(User.username==field.data).first():
            raise ValidationError("用户名重复")
