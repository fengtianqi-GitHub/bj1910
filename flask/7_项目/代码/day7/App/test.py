# -*- coding: utf-8 -*-
# @File    : test.py
# 描述     ：
# @Time    : 2020/1/7 11:50
# @Author  : 
# @QQ      :  

def demo(**kwargs):
    print(kwargs)
demo(a=1,b=2)
demo(**{'a':90,'b':80})