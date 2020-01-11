# -*- coding: utf-8 -*-
# @File    : models.py
# 描述     ：
# @Time    : 2020/1/7 9:40
# @Author  : 
# @QQ      :
from sqlalchemy.sql.functions import now

from .ext import db

class User(db.Model):
    uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(60),unique=True)
    password_hash = db.Column(db.String(128),nullable=False)
    sex = db.Column(db.SmallInteger,default=0)
    portrait = db.Column(db.String(200))
    regtime = db.Column(db.DateTime)
    __tablename__ = 'bbs_user'  # 数据库中表名

    def __str__(self):
        return "用户名：{} 性别:{}".format(self.username,self.sex)

