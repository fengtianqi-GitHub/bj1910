# -*- coding: utf-8 -*-
# @File    : settings.py
# 描述     ：
# @Time    : 2020/1/7 9:19
# @Author  : 
# @QQ      :  

# 短信验证配置
ACCESS_KEY_ID = "LTAIDHOYSjYcvyVt"  #用户AccessKey  需要根据自己的账户修改
ACCESS_KEY_SECRET = "qrEgykmXX4e6GUMFOqzuiLZ5gsUxSC"  #Access Key Secret  需要根据自己的账户修改

# 数据库连接参数
database = {
    'host':'47.88.225.157',
    'user':'python',
    'password':'123',
    'db':'bj1910',
    'port':'3306'
}
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}".format(**database)
SQLALCHEMY_TRACK_MODIFICATIONS = False

