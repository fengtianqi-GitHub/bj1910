import hashlib
from random import randint

from flask import Blueprint, render_template
from sqlalchemy import func, or_
from sqlalchemy.orm import aliased

from App.models import User,Caetgory
from ext import db


bbs = Blueprint('bbs',__name__)



@bbs.route('/index/')
@bbs.route('/index/<int:cid>')
def index(cid=0):
    # categories = Caetgory.query.filter(Caetgory.pid == 0).all()
    #
    # #展示指定版块
    # if cid == 0:
    #     bigCategory = categories
    # else:
    #     bigCategory = Caetgory.query.filter(Caetgory.cid == cid).all()
    #
    # smallCategory = Caetgory.query.filter(Caetgory.pid != 0).all()
    #
    # for big in bigCategory:
    #     print(big)

    categories = Caetgory.all_big()
    bigCategory,smallCategory = Caetgory.big_and_small(cid)
    return render_template('index.html',**locals())


@bbs.route('/list/<int:cid>/')
def list_forum(cid):
    return "list"



# 1表的创建和删除
@bbs.route('/create')
def create_table():
    db.create_all()
    return "创建表"

@bbs.route('/drop/')
def delete_table():
    #删除创建的所有的表
    db.drop_all()
    return "删除表"

# 增加记录
@bbs.route('/add/')
def add():
    # 插入一条记录
    # try:
    #     # user = User(username='admin',password_hash=hashlib.sha1(b'123').hexdigest())
    #     user = User()
    #     #非空的没有缺省值的属性必须赋值
    #     user.username = 'tom'
    #     user.password_hash = hashlib.sha1(b'123').hexdigest()
    #     db.session.add(user)
    #     # 默认开启了事务，需要手动提交
    #     db.session.commit()
    # except Exception as e:
    #     print(e)
    #     db.session.rollback()

    # try:
    #     bulk = []
    #     for i in range(10):
    #         user = User()
    #         user.username = 'test' + str(i)
    #         num = str(randint(100000,10000000))
    #         user.password_hash = hashlib.sha1(num.encode('utf8')).hexdigest()
    #         bulk.append(user)
    #     # 批量插入
    #     db.session.add_all(bulk)
    #     db.session.commit()
    # except Exception as e:
    #     print(e)
    #     db.session.rollback()

    #封装后的写法
    user = User()
    user.username = '李鹏'
    user.password_hash = hashlib.sha1(b'3453').hexdigest()
    user.save()

    return "插入记录"

# 修改
@bbs.route('/update/<int:uid>/')
def update_user(uid):
    #查询指定pk（主键）的记录
    # user必须是User的对象才能修改
    user = User.query.get(uid)
    if user:
        user.username = '哈哈哈'
        db.session.add(user)
        db.session.commit()
    print(user,type(user))
    return "修改记录"
# 删除
@bbs.route("/delete/<int:uid>/")
def delete_user(uid):
    # try:
    #     user = User.query.get(uid)
    #     db.session.delete(user)
    #     db.session.commit()
    # except Exception as e:
    #     print(e)
    #     db.session.rollback()

    user = User.query.get(uid)
    User.query.all()
    user.delete()
    return "删除记录"

#单表查询
@bbs.route('/query/')
@bbs.route('/query/<int:uid>')
def find(uid=1):
    # 1.返回一个记录
    # data = User.query.get(uid)
    # data = db.session.query(User).get(uid)

    #2 all
    # data = User.query.all()
    # if data:
    #     # 切片
    #     data = data[2:5]
    # print(data)

    #3 指定字段列表 [(字段1,字段2..)...]
    # data = User.query.with_entities(User.username,User.password_hash).all()
    # print(data)

    # 4去重 distinct
    # data = User.query.with_entities(User.sex).distinct().all()

    #5 别名
    # data = User.query.with_entities(User.username.label('name'),User.sex).all()
    # us = aliased(User,name='us')
    # data = db.session.query(us).all()

    #6 排序
    # 默认升序排序
    # data = User.query.order_by(User.sex).all()
    # data = User.query.order_by(User.sex.desc()).all()  #降序
    # #多字段排序
    # # data = User.query.order_by(-User.sex,-User.uid).all()
    # for rec in data:
    #     print(rec)

    # 聚合函数的用法
    # data = db.session.query(func.max(User.username)).all()
    # data = db.session.query(func.min(User.username)).all()
    # data = db.session.query(func.sum(User.sex)).scalar()
    # data = db.session.query(User).count()

    # 分组
    #select sex ,count(*) num from bbs_user group by sex having num>2
    # num = func.count('*')  #取字段别名
    #
    # data = db.session.query(User.sex,num,func.max(User.sex)).group_by(User.sex).having(num>2).all()

    # limit
    # data = User.query.limit(2).all()
    # data = User.query.offset(2).limit(2).all()

    #where filter
    # data = User.query.filter(User.sex==0).all()
    # data = User.query.filter(User.sex>0).all()
    # data = User.query.filter(User.username.like('%8')).all()
    # data = User.query.filter(User.username.like('test%')).all()
    # data = User.query.filter(User.uid.in_([2,3,5,9])).all()
    # uid not in [2,3,5,9]
    # data = User.query.filter(~User.uid.in_([2,3,5,9])).all()
    # data = User.query.filter(User.uid.notin_([2,3,5,9])).all()

    # is null
    # data = User.query.filter(User.birthday == None,User.sex == 0).all()

    # or
    # data = User.query.filter(or_(User.uid==3,User.uid==5)).all()
    # select * from bbs_user where (uid=3 or uid =4) and sex=1
    # data = User.query.filter(or_(User.uid==3,User.uid==4),User.sex==1).all()

    data = Caetgory.query.all()
    print(data)
    return "查询结果"