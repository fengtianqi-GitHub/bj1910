import re

# from urls import urlpatterns

urlpatterns = []

def wappter(rule):
    def inner(func):
        pattern = (rule,func)
        #注册路由
        urlpatterns.append(pattern)
        return func
    return inner

# @wappter(r'^/login$')
def login(environ,startResponse):
    startResponse('200 ok', [('Content-Type', 'text/html')])
    return [b'Login']
pf = wappter(r'^/login$')
pf(login)
print(urlpatterns)


def application(environ,startResponse):
    # for key in environ:
    #     print(key,'-----',environ[key])

    #1 获取请求路径
    path = environ.get('PATH_INFO','/')
    print(path)
    # 路由，根据用户不同的请求路径，调用不同处理方法进行处理
    # if path == '/':
    #     #首页
    #     return views.index(environ,startResponse)
    # elif path == '/login': #登陆处理
    #     return views.login(environ,startResponse)
    #第二版路由
    for pattern,func in urlpatterns:
        print(pattern,func)
        if re.match(pattern,path):
            return  func(environ,startResponse)


    startResponse('404 ok',[('Content-Type','text/html')])

    return ['<html><head><meta charset="utf-8"></head><body><h2>File Not Found</h2></body></html>'.encode('utf-8')]