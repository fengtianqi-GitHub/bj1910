from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    print("app02的首页")
    return HttpResponse("app02的首页----我返回我光荣")


def do_ajax(request):
    return {'code':1,'status':'sucess'}