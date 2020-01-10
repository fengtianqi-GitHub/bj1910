# -*- coding: utf-8 -*-
# @File    : models.py
# 描述     ：
# @Time    : 2020/1/10 9:18
# @Author  : 
# @QQ      :  

from extensions import db


class DbBase:
    # 添加⼀一条数据
    def save(self):
        try:
            db.session.add(self)  # 添加⼀一条数据
            db.session.commit()  # 提交
        except:
            db.session.rollback()

    # 添加多条数据
    @staticmethod
    def save_all(*args):
        try:
            db.session.add_all(args)
            db.session.commit()
        except:
            db.session.rollback()

    # 删除⼀一条数据
    def delete(self):
        try:
            db.session.delete(self)  # 添加⼀一条数据
            db.session.commit()  # 提交
        except:
            db.session.rollback()

class User(db.Model,DbBase):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,name='uid')
    username = db.Column(db.String(60),unique=True)
    password = db.Column(db.String(128),nullable=False,name='password_hash')
    sex = db.Column(db.Integer)

    __tablename__ = 'bbs_user'

class Post(db.Model,DbBase):
    id = db.Column(db.Integer,primary_key=True)
    tid =db.Column(db.Integer)
    authorid= db.Column(db.Integer)
    title = db.Column(db.String(1000))
    __tablename__ = 'bbs_post'

"""
create table bb_user(uid int primary key auto_increment,username varchar(60),password_hash)
"""