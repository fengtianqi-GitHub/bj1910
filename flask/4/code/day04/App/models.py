# 模型层，创建模型
from datetime import time

from ext import db

class BaseModel:
    #保存记录
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return  True
        except Exception as e:
            db.session.rollback()
            return False
    #保存多条记录
    @staticmethod
    def save_all(objlists):
        """

        :param objlists: 对象的列表
        :return:
        """
        try:
            db.session.add_all(objlists)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            db.session.rollback()
            return False


class User(db.Model,BaseModel):
    uid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(60),unique=True)
    password_hash = db.Column(db.String(128),nullable=False)
    sex =      db.Column(db.Integer,default=0)
    birthday = db.Column(db.DATE)
    realname = db.Column(db.String(60))
    portrait = db.Column(db.String(200))
    regtime  = db.Column(db.DATETIME)
    qq = db.Column(db.String(15))
    signature = db.Column(db.String(300))
    answer = db.Column(db.String(300))
    isactive = db.Column(db.Boolean,default=False)  #是否激活
    email = db.Column(db.String(300))
    __tablename__ = 'bbs_user'

    def __str__(self):
        return str(self.uid)+"---" + self.username +"---"+str(self.sex)+ "---" + self.password_hash



class Caetgory(db.Model,BaseModel):
    cid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    categoryname = db.Column(db.String(100),unique=True,nullable=False)
    pid = db.Column(db.Integer,nullable=False)
    themenum = db.Column(db.Integer,default=0)
    replynum = db.Column(db.Integer,default=0)
    lastpost = db.Column(db.String(200),nullable=True)
    compere = db.Column(db.String(20))
    startdate = db.Column(db.Date)
    __tablename__ = 'bbs_category'

    def __str__(self):
        return self.categoryname + "---" + str(self.cid)

    # 获取所有大版块
    @classmethod
    def all_big(cls):
        return cls.query.filter(cls.pid == 0)

    # 根据cid的值获取大小版块
    @classmethod
    def big_and_small(cls,cid=0):
        if cid == 0:
            bigs = cls.all_big()
            smalls = cls.query.filter(cls.pid != 0)
        else:
            bigs = cls.query.filter(cls.cid == cid)
            smalls = cls.query.filter(cls.pid == cid)
        return bigs,smalls