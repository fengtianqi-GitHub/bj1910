import json

from flask import Blueprint, render_template
from App.models import *
from App.example import *
from App.ext import  cache
bbs = Blueprint('bbs',__name__)

#缓存函数
@cache.cached(timeout=30,key_prefix='category')
def get_category():
    return Category.query.all()


@bbs.route('/index/')
# @cache.cached(timeout=10,key_prefix='index')
def index():
    # ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # return ts

    return render_template('index.html',bigs=get_category())

@bbs.route('/data/')
def cache_data():
    #到缓存中获取数据
    data = cache.get("bigCategory")

    if data:
        # json.loads
        data = json.loads(data)
        print(data)
        data = [json.loads(item) for item in data]
        print(data)
        return render_template('index.html',bigs=data)
    else:
        # 访问mysql
        data1 = Category.query.all()
        data = [item.to_json() for item in data1]
        data = json.dumps(data)
        cache.set('bigCategory',data)

        return render_template('index.html',bigs=data1)
    # data = Category.query.all()
    # print(data)
    # data = [item.to_json() for item in data]
    # print(data)
    # data = json.dumps(data)
    # print(data,type(data))
    # return "data"


@bbs.route('/one2many/')
def one2many():
    #插入数据
    # category = Category(categoryname='python基础',pid=0)
    # category.save()
    # user = User(username='admin',password_hash='1111')
    # user.save()

    category = Category.query.get(1)
    user = User.query.get(1)
    # #插入帖子
    # p1 = Posts(title='基础语法简单吗？')
    # p1.uid = user.uid
    # p2 = Posts(title='我用python')
    # p2.uid = user.uid
    # 通过版块保存帖子
    # category.posts = [p1,p2]
    # category.save()

    # p1 = Posts(title='装饰器是杀东东')
    # p1.uid = user.uid
    # p1.category = category
    # p1.save()
    # p2 = Posts(title='web')
    # p2.uid = user.uid
    # p2.category = category
    # p2.save()

    # 查询
    # 查询版块的帖子
    data = category.posts.filter(Posts.pid<3).all()
    # print(category.posts)
    # print(data)
    # # 又帖子查版块
    p1 = data[1]
    # print(p1.category.categoryname)
    # print(p1)

    # 级联删除
    c2 = Category.query.get(2)
    c2.delete()


    return "onetomany"

@bbs.route('/one2one/')
def one2one():
    # stu = Student(sname='小三')
    # db.session.add(stu)
    # db.session.commit()

    s1 = Student.query.get(2)
    # print(s1)
    # detail = Detail(nickyname="dkklsdlkds")
    # detail.sno = s1.sno
    # # detail.stu = s1
    # db.session.add(detail)
    # db.session.commit()
    # student->detial
    print(s1.detail.nickyname)

    #detail->student
    detail = Detail.query.get(2)
    print(detail.stu.sname)


    return "one to one"


@bbs.route("/many2many/")
def many2many():

    # student = Student.query.get(2)
    # c1 = Course.query.get(1)
    # c2 = Course.query.get(2)
    # print(student)
    # print(c1,c2)
    #
    # #学生选课
    # student.courses = [c1,c2]
    # db.session.add(student)
    # db.session.commit()
    # stu = Student.query.get(1)
    # print(stu)
    # #查看学生选课情况
    # print(stu.courses,type(stu.courses))

    course = Course.query.get(2)
    print(course.students)

    return "many to many"

@bbs.route('/join/')
def query_1():

    #1 内链接
    # data = db.session.query(Category,Posts).filter(Category.cid == Posts.cid,Posts.pid<6).all()
    # data = db.session.query(Category).join(Posts).filter(Category.cid == Posts.cid,Posts.pid<6)
    # data = db.session.query(Category,Posts,User).filter(Category.cid==Posts.cid,Posts.uid==User.uid)

    # 外链接
    # data = Category.query.outerjoin(Posts).all()
    # data = db.session.query(Category.categoryname,Category.pid).outerjoin(Posts).all()
    # data = db.session.query(Category).outerjoin(Posts)

    # 并
    data1 = Category.query.filter(Category.cid <= 3)
    data2 = Category.query.filter(Category.cid > 1)
    # data = data1.union(data2).all()

    #交
    # data = data1.intersect_all(data2).all()
    # print(data,type(data))

    #原生sql
    # data = db.session.execute("select * from bbs_category c left join bbs_posts p on c.cid=p.cid").fetchall()
    # :cid占位符
    # data = db.session.execute("select * from bbs_category c where cid = :cid",params={'cid':3}).fetchall()
    # print(data)
    return "query"
