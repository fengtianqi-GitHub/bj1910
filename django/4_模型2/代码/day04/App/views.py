import hashlib

from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import User, Post
from App.models2 import Student, Archive, Publisher, Book


def home(request):
    # 增加记录的快捷方式
    # User.objects.create(username="你咋又困了",password_hash="123")
    # user = User(username='2020年')
    # user.password_hash = hashlib.sha3_224(b'123').hexdigest()
    # user.save()
    # User.objects.bulk_create([User(username='111111',password_hash='222'),User(username='rrdddd',password_hash='222')])
    # update
    # user = User.objects.all().first()
    # user.username = "给你改个名"
    # user.save()

    # User.objects.filter(username__regex=r'^测试').update(grade=50)

    # 查询
    # select * from bbs_user
    # data = User.objects.all()

    # select username,password_hash from bbs_user
    # data = User.objects.values('username','password_hash')

    # distinct
    # data = User.objects.values("sex").distinct()

    # 统计函数
    # select count(sex) from bbs_user
    # data = User.objects.aggregate(Count('sex'))

    # 条件查询
    # data = User.objects.get(pk=210)  #f返回User对象
    #select * from bbs_user where
    # 关系运算符
    # data = User.objects.filter(sex=2,grade__gte=50)
    # between and
    # data = User.objects.filter(uid__range=[210,230])

    # in
    # data = User.objects.filter(uid__in=[210,223,234])

    # is null
    # data = User.objects.filter(sex=None)

    # like
    # data = User.objects.filter(username__iregex=r'试')

    # orderby
    # data = User.objects.all().order_by('-uid')
    # group by
    # data = User.objects.values('sex').annotate(num=Count('uid'))


    # limit
    # data = User.objects.all()[:3]   # limit 3
    # data = User.objects.all()[10:20] # limt 10,10

    # 子查询
    # 发了帖子的用户的用户名
    # result = Post.objects.values('authorid').distinct()
    # data = User.objects.filter(uid__in=result)
    # print(data.query)

    # 联合查询
    # 使用视图
    # 使用原生sql
    data = User.objects.raw("select * from bbs_user u join bbs_post p on u.uid=p.authorid join bbs_category c on c.cid=p.classid")
    # print(data.query)
    # print(list(data))
    # print(data)
    for rec in data:
        print(rec.classname,rec.username,rec.title)

    return HttpResponse("home")


def one2one(request):
    # student = Student.objects.first()
    # 增加一个学生
    # student = Student(sname="hello")
    # student.save()
    # print(student.sno)
    # 增加档案信息
    # archive = Archive(address="武汉")
    # archive.student = Student.objects.get(pk=3)
    # archive.save()

    # student=>archive
    # data = Student.objects.first().archive
    # data = Archive.objects.filter(student=Student.objects.get(pk=1).sno).first()

    # archive = >
    # data = Archive.objects.first().student
    # print(data)

    #夸关系查
    # archive__address
    # data = Student.objects.filter(archive__address='bj')
    data = Archive.objects.filter(student__sno=3)
    print(data)

    return HttpResponse("one to one")


def one2many(request):
    # publisher = Publisher.objects.create(pname='科学技术出版社')
    # print(publisher.pid)
    # add book
    pub = Publisher.objects.first()
    # pub.books.create(bname="高数")

    # publisher = > book
    # data = pub.books.all()

    # book=>publisher
    data = Book.objects.first()
    print(data.publisher)
    return HttpResponse("one to many")