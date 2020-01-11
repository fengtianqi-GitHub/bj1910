# -*- coding: utf-8 -*-
# @File    : exampe01.py
# 描述     ：第一个tornado应用
# @Time    : 2020/1/10 11:37
# @Author  : 
# @QQ      :
import tornado.web
import tornado.httpserver
import tornado.ioloop

# 用户请求处理类
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("自古深情留不住")
    def post(self):
        self.write("唯有套路得人心")
if __name__ == '__main__':
    app = tornado.web.Application([(r'/',IndexHandler)])
    # app.listen(8000) # 监听的端口

    # 创建web服务器，监听端口
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8000)

    print("服务器启动了.....")
    # 启动web服务器，监听端口，处理用户请求
    tornado.ioloop.IOLoop.current().start()

