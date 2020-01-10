# -*- coding: utf-8 -*-
# @File    : example03.py
# 描述     ：
# @Time    : 2020/1/10 14:35
# @Author  : 
# @QQ      :  

import tornado.web
import tornado.ioloop
import tornado.options
from settings import config
from tornado.web import url

# 定义命令行参数
tornado.options.define('port', default=8000, type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
        # self.write("首页")


class LoginHandler(tornado.web.RequestHandler):
    # 接收路由的第三个参数：字典中的键值对
    def initialize(self,hello):
        self.hello = hello

    def get(self):
        print(self.hello)
        # 路由的名称求出请求路径
        print(self.reverse_url('login'))
        self.write("login")


class ShowHandle(tornado.web.RequestHandler):
    def get(self,name,age):
        print(name,age)
        self.write("{}--{}".format(name,age))


class ListHandler(tornado.web.RequestHandler):
    def get(self,num):
        self.write(num)


def main():
    tornado.options.parse_command_line()
    # print(config)

    # 路由
    app = tornado.web.Application([(r'/', IndexHandler),
                                   url(r'/login',LoginHandler,{'hello':'tom'},name='login'),
                                   # 路由传参
                                   (r'/show/(\w+)/(\d+)',ShowHandle),
                                   (r'/list/(?P<num>\d+)',ListHandler)
                                   ], **config)
    # 从命令行接收的参数
    print(tornado.options.options.port)
    app.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()