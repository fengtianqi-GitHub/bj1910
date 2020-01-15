from django.db import models

# 自定义管理器类
class MyManager(models.Manager):
    def get_queryset(self):
        # 不查询逻辑删除的帖子
        return super().get_queryset().filter(isdel=0)




# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60,unique=True)
    # db_column 如果属性名和表中字段名不一致，需要设置db_column,db_column是表中的字段名
    password = models.CharField(max_length=128,db_column='password_hash')
    sex = models.IntegerField(choices=((1,'男'),(2,'女')),default=1)
    allowlogin = models.IntegerField()



    def __str__(self):
        return f"{self.username}:{self.sex}"

    class Meta:  # 表自身信息（元信息）
        db_table = 'bbs_user'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=60, blank=True, null=True)
    parentid = models.IntegerField()
    replycount = models.SmallIntegerField(blank=True, null=True)
    forumcount = models.SmallIntegerField(blank=True, null=True)
    compere = models.CharField(max_length=20, blank=True, null=True)
    classpic = models.CharField(max_length=200, blank=True, null=True)
    descrition = models.CharField(max_length=200, blank=True, null=True)
    orderby = models.SmallIntegerField(blank=True, null=True)
    lastpost = models.CharField(max_length=3000, blank=True, null=True)
    ispass = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbs_category'


class Closeip(models.Model):
    ip = models.IntegerField()
    addtime = models.IntegerField()
    overtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbs_closeip'


class Link(models.Model):
    lid = models.SmallIntegerField(primary_key=True)
    displayorder = models.IntegerField()
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    addtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bbs_link'


class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    tid = models.IntegerField()
    rate = models.IntegerField()
    addtime = models.IntegerField()
    ispay = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bbs_order'


class Post(models.Model):
    tid = models.IntegerField(blank=True, null=True)
    authorid = models.IntegerField()
    title = models.CharField(max_length=600)
    content = models.TextField()
    addtime = models.IntegerField()
    addip = models.IntegerField()
    classid = models.IntegerField()
    replycount = models.IntegerField()
    hits = models.IntegerField()
    istop = models.IntegerField()
    elite = models.IntegerField()
    ishot = models.IntegerField()
    rate = models.SmallIntegerField()
    attachment = models.SmallIntegerField(blank=True, null=True)
    isdel = models.IntegerField()
    style = models.CharField(max_length=10, blank=True, null=True)
    isdisplay = models.IntegerField()

    # 自定义管理器
    other = MyManager()

    class Meta:
        managed = False
        db_table = 'bbs_post'


class Reply(models.Model):
    tid = models.IntegerField(blank=True, null=True)
    authorid = models.IntegerField()
    content = models.TextField()
    addtime = models.IntegerField()
    addip = models.IntegerField()
    classid = models.IntegerField()
    isdel = models.IntegerField()
    isdisplay = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bbs_reply'


# class BbsUser(models.Model):
#     uid = models.AutoField(primary_key=True)
#     username = models.CharField(unique=True, max_length=60,null=True)
#     password_hash = models.CharField(max_length=128)
#     usertype = models.IntegerField(blank=True, null=True)
#     sex = models.IntegerField(blank=True, null=True)
#     birthday = models.DateField(blank=True, null=True)
#     realname = models.CharField(max_length=60, blank=True, null=True)
#     portrait = models.CharField(max_length=200, blank=True, null=True)
#     regtime = models.DateTimeField(blank=True, null=True)
#     qq = models.CharField(max_length=15, blank=True, null=True)
#     signature = models.CharField(max_length=300, blank=True, null=True)
#     answer = models.CharField(max_length=300, blank=True, null=True)
#     isactive = models.IntegerField(blank=True, null=True)
#     email = models.CharField(max_length=300, blank=True, null=True)
#     lasttime = models.DateTimeField(blank=True, null=True)
#     allowlogin = models.IntegerField(blank=True, null=True)
#     grade = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bbs_user'

class V_post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10000)
    content = models.CharField(max_length=20000)
    username = models.CharField(max_length=60)
    classname = models.CharField(max_length=60)
    class Meta:
        db_table = 'v_post'

class V_3(models.Model):
    uname = models.CharField(max_length=60)
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=10000)
    cname = models.CharField(max_length=100)

    class Meta:
        db_table = 'v_3'
