# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BookInfo(models.Model):
    btitle = models.CharField(max_length=200)
    bpub_date = models.DateField(blank=True, null=True)
    bread = models.IntegerField(null=True)
    bcomment = models.IntegerField(null=True)
    bimage = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookinfo'

class Heroinfo(models.Model):
    hid = models.AutoField(primary_key=True)
    hname = models.CharField(max_length=50)
    book = models.ForeignKey(BookInfo, models.DO_NOTHING,related_name='heros', db_column='bid')

    class Meta:
        managed = False
        db_table = 'heroinfo'

    # StringRelatedField 获取的对象信息
    def __str__(self):
        return f"{self.hname}--{self.hid}"