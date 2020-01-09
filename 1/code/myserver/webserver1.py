from wsgiref.simple_server import make_server
from myApplication import application

server = make_server('localhost',9000,application)
print("服务器启动�")
server.serve_forever()