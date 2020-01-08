# -*- coding: utf-8 -*-
# @File    : models.py
# 描述     ：数据模型
# @Time    : 2020/1/7 14:11
# @Author  : 
# @QQ      :
from App.extensions import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,name='uid')
    username = db.Column(db.String(60))

    __tablename__ = 'bbs_user'



class Category(db.Model):
    cid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    classname = db.Column(db.String(60),nullable=False)
    parentid = db.Column(db.Integer,default=0)
    replycount = db.Column(db.Integer)
    compere = db.Column(db.String(200))
    forumcount = db.Column(db.Integer)
    classpic = db.Column(db.String(300))
    description = db.Column(db.String(3000),name='descrition')
    lastpost = db.Column(db.String(3000))
    __tablename__ = 'bbs_category'

    def __str__(self):
        return f"{self.classname}"
