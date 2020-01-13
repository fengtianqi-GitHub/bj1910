from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import User


def index(request):
    # return HttpResponse("年年岁岁奖相似，岁岁年年拿不到")
    # 访问数据库
    data = User.objects.all()
    print(data)
    return render(request,'index.html',context={
        'title':'百度',
        'content':'冰箱是怎么搬回去',
        'users':data
    })