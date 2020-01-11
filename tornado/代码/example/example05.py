# -*- coding: utf-8 -*-
# @File    : example05.py
# 描述     ：
# @Time    : 2020/1/10 15:50
# @Author  : 
# @QQ      :  


import tornado.web
import tornado.ioloop
import tornado.options
from settings import config


# 定义命令行参数
tornado.options.define('port',default=8000,type=int)
class IndexHandler(tornado.web.RequestHandler):
    def initialize(self):
        print("initialize")
    def prepare(self):
        print("prepare")
    def set_default_headers(self):
        print("set_default_headers")
    def on_finish(self) -> None:
        print("on_finish")
    def write_error(self, status_code, **kwargs):
        print("write_error")
        self.write("write_error")
    def get(self):
        print("get")
        self.send_error(404)
        self.render('index.html')
        # self.write("首页")


def main():
    tornado.options.parse_command_line()
    # print(config)


    # 从配置文件加载参数
    app = tornado.web.Application([(r'/',IndexHandler)],**config)
    # 从命令行接收的参数
    print(tornado.options.options.port)
    app.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    main()
