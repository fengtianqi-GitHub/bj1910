# -*- coding: utf-8 -*-
# @File    : test.py
# 描述     ：
# @Time    : 2020/1/6 14:36
# @Author  : 
# @QQ      :  

import os
ext = os.path.splitext("12.3.jpg")
print(ext)
if len(ext) > 1:
    ext = ext[1].lstrip('.')
    print(ext)
# print(os.path.splitext("123.jpg"))
print(os.path.getsize('settings.py'))