# -*- coding: utf-8 -*-
# @File    : chat.py
# 描述     ：聊天
# @Time    : 2020/1/10 16:48
# @Author  : 
# @QQ      :
import json

import tornado.web
import tornado.ioloop
import tornado.websocket
import requests   # 发起模拟请求

# 显示聊天界面
class ClentHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ServerHandler(tornado.websocket.WebSocketHandler):
    web_clients = set()
    def open(self, *args, **kwargs):
        self.web_clients.add(self)
    # 接收客户端消息
    def on_message(self, message):
        print(message)
        req = requests.post(url="http://openapi.tuling123.com/openapi/api/v2",
                            json={
                                "reqType": 0,
                                "perception": {
                                    "inputText": {
                                        "text": message
                                    },
                                },
                                "userInfo": {
                                    "apiKey": "ed5435dd22ff4722a23ef4702311f779",
                                    "userId": "csl"
                                }
                            })
        # print()
        # 解析字符串为字典
        data = json.loads(req.text)
        print(data['results'][0]['values']['text'])
        self.write_message(data['results'][0]['values']['text'])

def main():
    app = tornado.web.Application([(r'/',ClentHandler),
                                   (r'/ws',ServerHandler)],
                                  debug=True,
                                  template_path='templates'
                                  )
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
if __name__ == '__main__':
    main()