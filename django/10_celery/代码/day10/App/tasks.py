#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    任务文件，定义任务
@author:  
@contact: 
@file: tasks.py
@time: 2020/2/15 10:04 上午
'''
from celery.signals import task_success
from celery import shared_task
import time

# 自定义任务
from django.core.mail import send_mail

from day10.settings import EMAIL_HOST_USER


@shared_task
def intro(name,age):
    print("我是{},{}岁了".format(name,age))
    time.sleep(2)

@shared_task
def fib(n):
    num = 0
    n1 = n2 = 1
    for i in range(3,n+1):
        num = n1 + n2
        n1, n2 = n2, num
    return num


@task_success.connect(sender=fib)
def task_done_handler(sender=None,  result=None,**kwargs):
    print("异步获取结果{}".format(result))

# 异步发送邮件
@shared_task
def send(subject,content,receiver):
    """
    :param subject: 邮件主题
    :param content: 邮件内容
    :param receiver: 接收者,只能是字符串
    :return:
    """
    send_mail(subject,content,EMAIL_HOST_USER,recipient_list=[receiver])

@shared_task
def hello():
    print("武汉加油")
