from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from App.models import Bookinfo
from App.serializers import BookInfoSerializer
from App.filters import BookFilter

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