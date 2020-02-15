#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: celery.py
@time: 2020/2/15 10:03 上午
'''
from __future__ import absolute_import #绝对路径导入
from celery import Celery
from django.conf import settings
import os

#设置系统的环境配置用的是Django的
# 要根据自己工程的情况指定settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day10.settings")

#实例化celery, 参数是实例的名称，可以自己指定
app = Celery('mycelery')

app.conf.timezone = "Asia/Shanghai"

#指定celery的配置来源 用的是项目的配置文件settings.py
app.config_from_object("django.conf:settings")

#让celery 自动去发现我们的任务（task）
app.autodiscover_tasks() #你需要在app目录下 新建一个叫tasks.py（一定不要写错）文件