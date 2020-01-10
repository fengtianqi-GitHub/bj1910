# -*- coding: utf-8 -*-
# @File    : example04.py
# 描述     ：
# @Time    : 2020/1/10 14:58
# @Author  : 
# @QQ      :  


import tornado.web
import tornado.ioloop
import tornado.options
from tornado.web import url

from settings import config


# 定义命令行参数
tornado.options.define('port',default=8000,type=int)
class IndexHandler(tornado.web.RequestHandler):
    def get(self):

        # self.redirect('/list')
        # self.redirect('/list')
        print(self.reverse_url('list'))
        self.redirect(self.reverse_url('list'))
        # # get请求参数获取
        # print(self.get_argument('name',default=''))
        # print(self.get_arguments('a'))
        #
        # # self.request 请求对象
        # print(self.request.method)
        # print(self.request.remote_ip)
        # print(self.request.path)
        # set_header设置响应头信息
        # self.set_header('xss', '30')
        # self.render('index.html')


    def set_default_headers(self):
        pass
        # self.write("首页")
    def post(self):
        # 获取post参数
        print(self.get_body_argument('name',default=''))
        print(self.get_body_arguments('b'))
        self.write("post")
class ListHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("list")
        # self.redirect('/')


def main():
    tornado.options.parse_command_line()
    # print(config)


    # 从配置文件加载参数
    app = tornado.web.Application([(r'/',IndexHandler),
                                   url(r'/list',ListHandler,name='list')
                                   ],**config)
    # 从命令行接收的参数
    print(tornado.options.options.port)
    app.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    main()
