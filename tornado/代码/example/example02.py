# -*- coding: utf-8 -*-
# @File    : example02.py
# 描述     ：
# @Time    : 2020/1/10 14:12
# @Author  : 
# @QQ      :  

import tornado.web
import tornado.ioloop
import tornado.options
from settings import config


# 定义命令行参数
tornado.options.define('port',default=8000,type=int)
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
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
