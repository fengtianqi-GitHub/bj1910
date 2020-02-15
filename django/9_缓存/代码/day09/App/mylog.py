#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    日志操作
@author:  
@contact: 
@file: mylog.py
@time: 2020/2/14 4:15 下午
'''
import logging

# 生成一个日志对象
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
print(logger)

# 设置handler
# 日志文件
fileHandler = logging.FileHandler("log.txt")

# 指定一个日志格式
formatter = logging.Formatter("%(levelname)s  %(filename)s  %(lineno)d  %(asctime)s  %(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.info("hello")