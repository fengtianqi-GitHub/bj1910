#
# d1 = {'a':10,'b':'hello'}
# #get('键','默认值'),如果键不存在，不会报语法错;
# print(d1.get('c','20'))

# t1 = (1,2)
# a,b = t1
# print(a,b)
# import re
# s1 = "hello1243rere"
# pattern = r"123"
# print(re.search(pattern,s1))
# def world():
#     print("world")
# def hello():
#     print("hello")
#
# pf = hello
# pf()
# pf = world
# pf()

# def wapper(func):
#     def inner(*args,**kwargs):
#         print("------")
#         func(*args,**kwargs)
#
#     return inner
#
# @wapper   #hello = wapper(hello)
# def hello(name):
#     print("hello:{}".format(name))
#
# # hello = wapper(hello)
# hello("tom")


# hello()
urlpatterns = []

def wappter(rule):
    def inner(func):
        print(rule)
        print("*"*50)
        pattern = (rule,func)
        urlpatterns.append(pattern)
        return func
    return inner
#
@wappter('/')
def world():
    print("world")
# inner = wappter('/')
# def world():
#     print("world")
#
# inner = inner(world)


# print(urlpatterns)
# pf = wappter('/')
# # pf = inner
# pf(world)

