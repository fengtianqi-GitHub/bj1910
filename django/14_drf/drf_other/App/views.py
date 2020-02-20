# from rest_framework import Re
from django.contrib.auth.hashers import make_password
from rest_framework.generics import GenericAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from rest_framework.response import Response

from App.autentications import MyAuthentication
from App.models import Bookinfo
from App.serializers import BookInfoSerializer, UserSerializer


class BooksView(ListModelMixin,
                CreateModelMixin,
                RetrieveUpdateDestroyAPIView
                ):
    # 必须指定查询结果集
    queryset = Bookinfo.objects.all()
    serializer_class = BookInfoSerializer

    lookup_field = 'pk'  # 数据库中查询的字段名，pk表示主键
    lookup_url_kwarg = 'bid'


    def get(self,request,*args,**kwargs):
        if len(kwargs) > 0: # 查询指定对象
            return self.retrieve(request,*args,**kwargs)
        else: # 查询所有对象
            # data = self.queryset.all()
            # serializer = BookInfoSerializer(instance=data,many=True)
            # return Response(serializer.data)
            return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self,request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)


class IndexView(GenericAPIView):
    queryset = Bookinfo.objects.all()
    serializer_class = BookInfoSerializer
    # 局部认证
    authentication_classes = (MyAuthentication,)

    def get(self,request):
        return Response({"code":1})


class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        request.data._mutable = True  # 设置data数据可修改
        request.data['password'] = make_password(request.data['password'])
        return self.create(request, *args, **kwargs)
