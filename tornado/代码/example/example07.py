# -*- coding: utf-8 -*-
# @File    : example07.py
# 描述     ：
# @Time    : 2020/1/10 16:23
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
        self.render('login.html')
    def post(self):
        print(self.get_argument('username'))
        return "login"

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
