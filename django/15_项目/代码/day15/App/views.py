import os
from random import randint

from django.shortcuts import redirect
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,GenericAPIView
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from App.models import Bookinfo
from App.serializers import BookInfoSerializer
from App.filters import BookFilter
from alipay import AliPay



class BooksView(ListAPIView):
    """
    图书查询
    """
    queryset = Bookinfo.objects.all()
    serializer_class = BookInfoSerializer
    # 过滤类
    filter_class = BookFilter
    # http://127.0.0.1:8000/book/?bread=20&btitle=笑傲江湖
    # filter_fields = ('btitle','bread')


class ListView(RetrieveUpdateDestroyAPIView):
    """
    get:
    图书列表
    
    put:
    修改图书信息
    
    delete:
    删除图书
    """
    queryset = Bookinfo.objects.all()
    serializer_class = BookInfoSerializer


    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# 和支付相关
class AlipayView(GenericAPIView):
    # from day15.settings import APP_PRIVATE_KEY,APPID,ALI_PUBLIC_KEY


    def get(self,request,*args,**kwargs):
        from day15.settings import BASE_DIR
        ALI_PUBLIC_KEY = open(os.path.join(BASE_DIR, 'utils/ali_public_key.pem')).read()
        # # 应用程序私钥
        APP_PRIVATE_KEY = open(os.path.join(BASE_DIR, 'utils/app_private_key.pem')).read()
        # # 应用程序的appid
        APPID = "2016100100641498"
        # 生成支付对象
        alipay = AliPay(
            appid=APPID,
            app_notify_url="http://127.0.0.1:8000/notify/",  # 默认回调url
            app_private_key_string = APP_PRIVATE_KEY,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string = ALI_PUBLIC_KEY,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug = False  # 默认False
        )

        # 生成订单
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no= str(randint(100000,100000000)),
            total_amount=100,
            subject="nike运动鞋",
            return_url="http://127.0.0.1:8000/index/", # 支付成功后回调地址
            # 异步支付完成后，支付宝通知信息调用
            notify_url="http://127.0.0.1:8000/notify/"  # 可选, 不填则使用默认notify url
        )
        # 获取支付宝客户端url
        url = "https://openapi.alipaydev.com/gateway.do?" + order_string
        # print(url)
        # 实际开发中应该返回给客户端
        return redirect(url)


class IndexView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":'支付成功'})
    def post(self,request,*args,**kwargs):
        return Response({"msg": '支付成功'})


class NotifyView(GenericAPIView):
    def pos(self,request,*args,**kwargs):
        # for django users
        data = request.dict()
        # for rest_framework users
        data = request.data
        print(data)

        signature = data.pop("sign")

        from day15.settings import BASE_DIR
        ALI_PUBLIC_KEY = open(os.path.join(BASE_DIR, 'utils/ali_public_key.pem')).read()
        # # 应用程序私钥
        APP_PRIVATE_KEY = open(os.path.join(BASE_DIR, 'utils/app_private_key.pem')).read()
        # # 应用程序的appid
        APPID = "2016100100641498"
        # 生成支付对象
        alipay = AliPay(
            appid=APPID,
            app_notify_url="http://127.0.0.1:8000/notify/",  # 默认回调url
            app_private_key_string=APP_PRIVATE_KEY,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=ALI_PUBLIC_KEY,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug=False  # 默认False
        )

        # verification
        success = alipay.verify(data, signature)
        if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
            print("trade succeed")
        return Response({"code":1,'msg':"验证成功"})