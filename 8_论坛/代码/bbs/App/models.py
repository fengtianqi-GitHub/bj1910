# -*- coding: utf-8 -*-
# @File    : models.py
# 描述     ：数据模型
# @Time    : 2020/1/7 14:11
# @Author  : 
# @QQ      :
from App.extensions import db


class Category(db.Model):
    cid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    classname = db.Column(db.String(60),nullable=False)
    parentid = db.Column(db.Integer,default=0)
    replycount = db.Column(db.Integer)
    forumcount = db.Column(db.Integer)
    lastpost = db.Column(db.String(3000))
    __tablename__ = 'bbs_category'

    def __str__(self):
        return f"{self.classname}"
