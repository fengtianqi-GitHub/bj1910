#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: temp.py
@time: 2020/2/17 10:59 上午
'''

class Animal:
    def walk(self):
        print("walk")
    def eat(self):
        print("eat")

obj = Animal()
res = getattr(obj,'walk')
print(res,type(res))
res()