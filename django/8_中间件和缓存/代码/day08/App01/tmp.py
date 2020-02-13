#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: tmp.py
@time: 2020/2/13 11:12 上午
'''
import os
from datetime import datetime

filename = "1.jpg"
# splitext把文件名分割为两部分（不带后缀的文件名，".后缀名"）
# print(os.path.splitext(filename))
# ext = os.path.splitext(filename)
# ext = ext[1].lstrip('.')
# # print(ext)
# if ext not in ['bmp','png','jpeg']:
#     print("后缀命名不符合要求")
#
from day08 import settings
res = datetime.now().strftime("%Y/%m/%d")
res = os.path.join(settings.MEDIA_ROOT,res)
print(res)
if not os.path.exists(res):
    os.makedirs(res)