# from rest_framework import Re
import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from rest_framework.generics import GenericAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle

from App.MyPaginations import MyPagination
from App.autentications import MyAuthentication
from App.models import Bookinfo, User
from App.permissions import BookPermission
from App.serializers import BookInfoSerializer, UserSerializer
from App.throttles import IndexThrottle


class BooksView(ListModelMixin,
                CreateModelMixin,
                RetrieveUpdateDestroyAPIView
                ):
    # 必须指定查询结果集
    queryset = Bookinfo.objects.all()
    serializer_class = BookInfoSerializer
    # 后面的逗号必须有，因为后面是元组
    # authentication_classes = MyAuthentication,
    # permission_classes = BookPermission,

    lookup_field = 'pk'  # 数据库中查询的字段名，pk表示主键
    lookup_url_kwarg = 'bid'
    # 指定分页类
    pagination_class = MyPagination


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
    # authentication_classes = (MyAuthentication,)


    def get(self,request):
        return Response({"code":1})


class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        request.data._mutable = True  # 设置data数据可修改
        request.data['password'] = make_password(request.data['password'])
        return self.create(request, *args, **kwargs)


class UserLoginView(CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # 查询数据库，获取用户
        user = User.objects.filter(username=username).first()
        if user and check_password(password,user.password):
            # 登录成功
            # 生成token
            token = uuid.uuid4().hex  # 得到16进制字符串
            # 把用户id存入redis，token是键
            cache.set(token,user.id,3600*3)
            return Response({'code':1,'msg':'登录成功','token':token})
        else:
            return Response({'code':-1,'msg':'用户名或密码错误'})
        # {"code":1,"msg":"登录成功","token":"a8fedfe06a9940d196770900937dd741"}

# 获取新的token
class TokenView(GenericAPIView):
    def post(self,request,*args,**kwargs):
        # 获取原来的token
        old_token = request.data.get('token')
        token = uuid.uuid4().hex
        uid = cache.get(old_token)
        if uid:
            # 生成新token
            cache.set(token,uid,3600*3)
            return Response({'code':1,'msg':'获取成功','token':token})
        else:
            return Response({'code':-1,'msg':'token已过期，请重新你登录'})
