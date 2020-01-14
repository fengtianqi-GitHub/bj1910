# -*- coding: utf-8 -*-
# @File    : test.py
# 描述     ：
# @Time    : 2020/1/13 16:13
# @Author  : 
# @QQ      :  
# 任意位置参数
def demo(*args):
    print(args)
# demo()
# demo(1)
# demo(1,'333')
# demo(1,'333',4)

def demo1(**kwargs):
    print(kwargs)
# demo1()
# demo1(a=2)
# demo1(a=2,b=3)

import  re
# 无命名组 提取指定值

result = re.match(r'(\d{3,4})-(?P<no>\d{7,8})',"010-38737845")
print(result)
print(result.group(1))
print(result.group(2))
print(result.group('no'))



