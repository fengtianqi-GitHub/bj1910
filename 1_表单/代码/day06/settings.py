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

if __name__ == '__main__':
    print(BASEDIR)
    print(UPLOAD_FOLDER)
