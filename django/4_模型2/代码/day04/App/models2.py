# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Archive(models.Model):
    aid = models.AutoField(primary_key=True)
    idcard = models.CharField(max_length=18, blank=True, null=True)
    address = models.CharField(max_length=3000, blank=True, null=True)
    student = models.OneToOneField('Student', models.CASCADE, db_column='sno', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'archive'


class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=60, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Book(models.Model):
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    # related_name 通过出版社查询图书
    publisher = models.ForeignKey('Publisher', models.CASCADE, db_column='pid',related_name='books')

    class Meta:
        managed = False
        db_table = 'book'


class Publisher(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publisher'

class Video(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        abstract = True

class ChildVideo(Video):
    pass