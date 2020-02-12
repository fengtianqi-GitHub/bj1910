from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app02.forms import RegisterForm
from App01.models import User


def register(request):
    if request.method == 'POST':
        #验证数据
        #1.用提交过来的数据request.post生成表单对象
        form = RegisterForm(request.POST)
    #     2.通过form的is_valid来检测数据是否合格，合格返回True，否则返回False
        if form.is_valid():
            print(form.cleaned_data)
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            # user=User(username=username,password=password)
            # user.save()
            return HttpResponse('首页')
        else:
            print(form)
            print(3333)
            return render(request, 'app02/register.html', locals())
    else:
        #实例化表单对象 get请求
        form=RegisterForm()
        return render(request,'app02/register.html')