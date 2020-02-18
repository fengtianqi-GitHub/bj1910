from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from rest_framework.views import APIView

from App.models import BookInfo
from App.serializers import BookInfoSerializer


class BookInfoView(APIView):
    def get(self,request,bid):
        # bid = kwargs.get('id')
        # 1.查询数据库
        book = BookInfo.objects.filter(pk=bid).first()
        print(book)
        if book:
            # 2.序列化
            serializer = BookInfoSerializer(book)
            print(serializer.data)
            # 3.返回json字符串
            return Response(serializer.data)
        else:
            return Response({'code':0,'msg':'你查询的图书不存在'})


class BooksView(APIView):
    def get(self,request):
        books = BookInfo.objects.all()
        print(books)
        # 如果序列化的对象是查询结果集，则需要使用many=true
        serializer = BookInfoSerializer(books,many=True)
        print(serializer.data)
        return Response(serializer.data)