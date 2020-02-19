from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from App.models import BookInfo
from App.serializers import BookInfoSerializers


class IndexView(APIView):
    def get(self,request,*args,**kwargs):
        books = BookInfo.objects.all()
        # 序列化
        # 如果books是一个模型对象，则many不能设置为True
        # 如果books是一个查询结果集，必须把many设置为True
        print(books)
        serializer = BookInfoSerializers(instance=books,many=True)
        # 获取序列化的结果,会把转换为字典，把结果集转为列表
        print(serializer.data)
        res = Response(serializer.data)
        print(res,type(res))
        return res

    # 新增书籍
    def post(self,request,*args,**kwargs):
        print(request.data)
        # 反向序列化器 给data赋值
        serializer = BookInfoSerializers(data=request.data)
        # 查看验证是否通过
        if serializer.is_valid():
            # 获取验证后数据
            # print(serializer.validated_data)
            book = serializer.save()  # 保存到数据
            return Response({'code':1,'msg':'新增加成功','id':book.id})
        else:
            # 获取验证失败原因
            print(serializer.errors)
            return Response({'code':-1,'msg':serializer.errors})
    # 更新对象
    def put(self,request,bid):
        print(bid)
        # 查询记录
        book = BookInfo.objects.get(pk=bid)
        print(book)
        # 更新数据: 模型对象赋值instance，更新数据赋给data
        serializer = BookInfoSerializers(instance=book,data=request.data)
        if serializer.is_valid():
            res = serializer.save()  # 调用update
            return Response({"code":2,'msg':'更新成功'})
        else:
            return Response({'code':-1,"msg":serializer.errors})


class ReqView(APIView):
    def get(self,request):
        print(request,type(request))
        # GET请求
        print(request.query_params)
        # 获取get参数值
        print(request.query_params.get('kk'))
        print(request.method)
        return Response({'code':1})
    def post(self,request):
        print(request.data)
        # 获取POST\PUT|PATCH传参
        print(request.data.get('name'))
        return Response({'code': 1})
    def patch(self,request,num):
        print(request.data)
        # 获取POST\PUT|PATCH传参
        print(request.data.get('bread'))
        # bread = int(request.data.get('bread'))
        book = BookInfo.objects.get(pk=num)
        serializer = BookInfoSerializers(instance=book,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()

        return Response({'code': 1})

# 图书列表
class BooksView(ListAPIView):
    # 指定查询结果集
    queryset = BookInfo.objects.all()
    # 指定序列化器
    serializer_class = BookInfoSerializers

# 创建图书
class BooksView2(CreateAPIView):
    serializer_class = BookInfoSerializers

# 更新书籍信息
class BooksView3(UpdateAPIView):
    queryset = BookInfo.objects.all()
    # url中主键的名称
    lookup_url_kwarg = 'bid'
    # 数据库中查询的主键名称
    lookup_field = 'id'
    serializer_class = BookInfoSerializers

# 删除书籍
class BooksView4(DestroyAPIView):
    queryset = BookInfo.objects.all()
    # url中主键的名称
    lookup_url_kwarg = 'bid'
    # 数据库中查询的主键名称
    lookup_field = 'id'
    serializer_class = BookInfoSerializers


class BooksView5(ListAPIView,RetrieveAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializers
    # url中主键的名称
    lookup_url_kwarg = 'bid'
    # 数据库中查询的主键名称
    lookup_field = 'id'

    def get(self,request,*args,**kwargs):
        if len(kwargs) > 0:
            return self.retrieve(request,*args,**kwargs)
        else:
            return self.list(request,*args,**kwargs)