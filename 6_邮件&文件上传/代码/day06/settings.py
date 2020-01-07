# -*- coding: utf-8 -*-
# @File    : settings.py
# 描述     ：项目配置文件
# @Time    : 2020/1/6 9:23
# @Author  : 
# @QQ      :  

import os

# 得到系统当前的路径
BASEDIR = os.getcwd()

# 文件上传的目录
UPLOAD_FOLDER = os.path.join(BASEDIR,'static/upload')

# 文件上传限制
ALLOWED_SUFFIX = ['jpg','jpeg','png','bmp']  # 后缀限制
ALLOWED_MAX_SIZE = 1024 * 1024 * 2   # 大小限制，字节 最大2M


# 邮件配置
MAIL_SERVER = "smtp.qq.com"  # 邮箱服务器
MAIL_USERNAME = "313728420@qq.com"
MAIL_PASSWORD = 'lrpqrsrmlduabihf'  # 授权码
MAIL_PORT = 465  # 端口
MAIL_USE_SSL = True  # 加密发送


#数据库:
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://python:123@47.58.225.157:3306/bj1910"
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "SDSDMKFKSDRIUEWWIO7636qeius*((*9wq76eq"
if __name__ == '__main__':
    print(BASEDIR)
    print(UPLOAD_FOLDER)
