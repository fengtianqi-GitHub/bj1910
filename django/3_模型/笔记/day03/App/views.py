import hashlib

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from App.models import User


def home(request):
    # tp = loader.get_template("index.html")
    # html = tp.render()
    # return HttpResponse(html)
    num = 10
    name = 'happy new year'
    return render(request,'index.html',context=locals())


def create(request):
    return HttpResponse("新的一页")


def process(request):
    # 1.增加用户
    # User.objects.create(username='测试用户',password='123',sex=1)

    # 使用save保存
    # user = User(username='测试用户2')
    # user.password = hashlib.sha1("123".encode('utf8')).hexdigest()
    # user.save()

    # 批量插入
    # users = []
    # for i in range(10):
    #     user = User(username="测试用户"+str(i),password=str(i))
    #     users.append(user)
    # User.objects.bulk_create(users)

    # 2 更新记录
    # user = User.objects.get(pk=276)
    # if user:
    #     user.username = '大疆无人机'
    #     user.save()
    # print(user)
    # 更新多条(不要对多表查询做更新)
    # users = User.objects.filter(uid__gt=277)
    # print(type(users))
    # users.update(sex=2)

    # 删除
    user = User.objects.get(pk=277)
    user.delete()
    return HttpResponse("增删改")


def find(request):
    # all 查询所有记录
    users = User.objects.all()
    # print(users.__dict__)
    # filter where子句
    # filter 过滤器，可以串联调用
    # users = User.objects.filter(sex=2).filter(username__istartswith="测试")
    # t条件默认是与
    # select * from bbs_user where sex=2 and username like '测试%'
    # users = User.objects.filter(sex=2,username__istartswith="测试")

    # exclude 条件取反
    # users = User.objects.exclude(sex=1)

    # values获取指定字段
    # users = User.objects.all().values('username')

    # order
    # users = User.objects.all().order_by('-sex','password')

    # distinct 去重
    users = User.objects.values("sex").distinct()
    print(users.query)
    print(type(users))

    return render(request,'users.html',context=locals())


def query1(request):

    try:
        # get 查询单条记录,如果返回多条记录或不返回会引发异常
        # user = User.objects.get(sex=1)

        # first 返回结果集第一条记录,last结果集中最后一条
        # user = User.objects.filter(sex=1).first()
        # user = User.objects.filter(sex=1).last()

        # count 返回结果集中记录数
        # user = User.objects.count()
        # exists 查看结果集中是否存在记录
        user = User.objects.filter(sex=3).exists()
        return HttpResponse(str(user))
    except Exception as e:
        print(e)
        return HttpResponse(str(e))

