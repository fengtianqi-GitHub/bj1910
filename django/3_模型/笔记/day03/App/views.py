import hashlib

from django.db import connection
from django.db.models import Count, Max, Q, F
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from App.models import User, V_post, V_3, Post


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
        # user = User.objects.filter(sex=3).exists()

        # 查询结果集限制
        # user = User.objects.all()
        # if user:
        #     # user = user[2]  # 取第几条记录
        #     # user = user[1:3] # 切片  limit1,2
        #     # 不能使用负的下标
        #     user = user[10:1:-2] # 切片  limit1,2
        #     print(user)

        # 条件
        # 关系运算 gt > ; gte >=  lt < lte <=
        # user = User.objects.filter(uid__gt=200)
        # between and
        # 200<=uid<=210
        # user = User.objects.filter(uid__range=[200,210])

        # in
        # user = User.objects.filter(uid__in=[210,214,216])
        # is null
        # user = User.objects.filter(sex=None)

        # regex
        # user = User.objects.filter(username__regex=r'^w')  # 以w开头
        user = User.objects.filter(username__regex=r'd')  # 包含d
        # 分组和统计
        # num=Count('uid')  num就是统计字段的别名： {'num': 27}
        user = User.objects.aggregate(num=Count('uid'))
        # print(user.query)
        # 分组
        # value指定分组字段,annotate指定统计函数
        user = User.objects.all().values('sex').annotate(num=Count('uid'),max1=Max('uid'))
        print(user.query)
        print(user)
        return HttpResponse(str(user))
    except Exception as e:
        print(e)
        return HttpResponse(str(e))


def list_post(request):
    # 查询视图
    # data = V_post.objects.all()
    # print(data)
    # for post in data:
    #     print(post.__dict__)

    # v_3
    data = V_3.objects.all()
    return render(request,'post.html',context=locals())


def logic_or(request):
    # |
    """
    SELECT `bbs_user`.`uid`, `bbs_user`.`username`, `bbs_user`.`password_hash`, `bbs_user`.`sex` FROM `bbs_user` WHERE ((`bbs
_user`.`uid` = 200 OR `bbs_user`.`uid` = 205) AND `bbs_user`.`username` REGEXP BINARY ^w)
    """
    # data = User.objects.filter(Q(uid=200)|Q(uid=205),username__regex=r'^w')
    # print(data)
    # print(data.query)

    # F 表中两列做比较
    # data = User.objects.filter(sex=F('allowlogin'))


    # 原生sql
    # 迭代器
    # data = User.objects.raw("select * from bbs_user u join bbs_post p on u.uid=p.authorid")
    #
    # for v in data:
    #     print(v.username,v.title)
    # 带参数传递的raw
    # username = 'wywzjkl'
    # 可能会发生sql注入
    # username = "sddfsd' or '1"
    # data = User.objects.raw("select * from bbs_user where username='{}'".format(username))

    # 防止sql注入
    # username = "sddfsd' or '1"
    # data = User.objects.raw("select * from bbs_user where username=%s",[username])
    # print(data.query)
    # print(list(data))
    with connection.cursor() as cursor:
        # username = "sddfsd' or '1"
        username = "lykzm"
        cursor.execute("select * from bbs_user where username=%s ",[username])
        print(cursor.fetchall())
    return HttpResponse("逻辑或")


def custom_manager(request):
    # data = User.other.all()
    # print(data)
    # 用自定义管理查询
    data = Post.other.all().values('isdel')
    print(list(data))
    return HttpResponse("自定义管理")