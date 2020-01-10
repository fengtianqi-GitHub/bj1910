# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Integer, SmallInteger, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class BbsCategory(db.Model):
    __tablename__ = 'bbs_category'

    cid = db.Column(db.Integer, primary_key=True)
    classname = db.Column(db.String(60))
    parentid = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    replycount = db.Column(db.SmallInteger, server_default=db.FetchedValue())
    forumcount = db.Column(db.SmallInteger, server_default=db.FetchedValue())
    compere = db.Column(db.String(20))
    classpic = db.Column(db.String(200), server_default=db.FetchedValue())
    descrition = db.Column(db.String(200))
    orderby = db.Column(db.SmallInteger)
    lastpost = db.Column(db.String(3000))
    ispass = db.Column(db.Integer, server_default=db.FetchedValue())



class BbsCloseip(db.Model):
    __tablename__ = 'bbs_closeip'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    overtime = db.Column(db.Integer)



class BbsLink(db.Model):
    __tablename__ = 'bbs_link'

    lid = db.Column(db.SmallInteger, primary_key=True)
    displayorder = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    name = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String)
    logo = db.Column(db.String(255))
    addtime = db.Column(db.Integer, nullable=False)



class BbsOrder(db.Model):
    __tablename__ = 'bbs_order'

    oid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    tid = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    ispay = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否已付款')



class BbsPost(db.Model):
    __tablename__ = 'bbs_post'

    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.Integer)
    authorid = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(600), nullable=False)
    content = db.Column(db.String, nullable=False)
    smiley = db.Column(db.SmallInteger)
    addtime = db.Column(db.Integer, nullable=False)
    addip = db.Column(db.Integer, nullable=False)
    classid = db.Column(db.Integer, nullable=False)
    replycount = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    hits = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    istop = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    elite = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    ishot = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    rate = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    attachment = db.Column(db.SmallInteger)
    isdel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    style = db.Column(db.String(10))
    isdisplay = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class BbsReply(db.Model):
    __tablename__ = 'bbs_reply'

    id = db.Column(db.Integer, primary_key=True)
    tid = db.Column(db.Integer)
    authorid = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String, nullable=False)
    addtime = db.Column(db.Integer, nullable=False)
    addip = db.Column(db.Integer, nullable=False)
    classid = db.Column(db.Integer, nullable=False)
    isdel = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    isdisplay = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())



class BbsUser(db.Model):
    __tablename__ = 'bbs_user'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    usertype = db.Column(db.Integer, server_default=db.FetchedValue())
    sex = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    realname = db.Column(db.String(60))
    portrait = db.Column(db.String(200))
    regtime = db.Column(db.DateTime)
    qq = db.Column(db.String(15))
    signature = db.Column(db.String(300))
    answer = db.Column(db.String(300))
    isactive = db.Column(db.Integer)
    email = db.Column(db.String(300))
    lasttime = db.Column(db.DateTime)
    allowlogin = db.Column(db.Integer, server_default=db.FetchedValue())
    grade = db.Column(db.Integer, server_default=db.FetchedValue())
