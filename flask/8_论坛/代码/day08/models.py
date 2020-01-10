# -*- coding: utf-8 -*-
# @File    : models.py
# 描述     ：数据模型
# @Time    : 2020/1/8 9:20
# @Author  : 
# @QQ      :  

from extensions import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,name='uid')
    username = db.Column(db.String(60),unique=True)
    password = db.Column(db.String(120),nullable=False,name='password_hash')

    __tablename__ = 'bbs_user'

    def __str__(self):
        return "{username}--{password}".format(username=self.username,password=self.password)
