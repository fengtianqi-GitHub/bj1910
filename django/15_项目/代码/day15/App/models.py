# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime

from django.db import models


class Bookinfo(models.Model):
    btitle = models.CharField(max_length=200,verbose_name='标题')
    bpub_date = models.DateField(blank=True, null=True,verbose_name='出版日期')
    bread = models.IntegerField(null=True,verbose_name='阅读数量')
    bcomment = models.IntegerField(null=True,verbose_name='评论数量')
    bimage = models.CharField(max_length=200, blank=True, null=True,verbose_name='图片')

    class Meta:
        managed = False
        db_table = 'bookinfo'
        verbose_name = "图书"


class Heroinfo(models.Model):
    hid = models.AutoField(primary_key=True)
    hname = models.CharField(max_length=50)
    book = models.ForeignKey(Bookinfo, models.DO_NOTHING, db_column='bid',related_name='heros', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'heroinfo'


class User(models.Model):
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    usertype = models.IntegerField(choices=[(1,'超管'),(2,'管理员'),(3,'普通用户')],default=3)
    email = models.CharField(max_length=254, blank=True, null=True)
    date_joined = models.DateTimeField(default=datetime.now)

    class Meta:
        managed = False
        db_table = 'user'
