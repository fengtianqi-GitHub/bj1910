# d1 = {'a':10,'b':'hello'}
#
# def demo(a=1,b=3):
#     # print(kwargs)
#     print(a,b)
#
# # demo(a=1,b=3)
# demo(**d1)

a,b = (3,4)
# b,c = [9,10]
def hello():
    a = 1
    b = 3
    print(locals())

hello()