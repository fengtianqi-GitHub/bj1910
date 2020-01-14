from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


def load_template(request):
    # # 获取模板对象
#     # template = loader.get_template("app2/load.html")
#     # print(template)
#     # list1 = [1,2,3,4]
#     # html = template.render(context={'list1':list1})
#     # print(html)
#     # return HttpResponse(html)
    return render(request,"app2/load.html",context={'list1':[1,2,3,4,5]})


def show_var(request):
    a = 10
    s1 = "考勤"
    list1 = [10,20,30]
    d1 = {'name':'质量','h5':'王大神'}
    # locals局部变量字典
    return render(request,"app2/1_var.html",context=locals())


def use_filter(request):
    num = 10
    name = 'jerry'
    content = "<h2>帝国的坟场</h2>"
    content2 = "<u>塔利班</u>"
    return render(request,'app2/2_filter.html',context=locals())


def define_inner(request):
    num = 10
    # list1 = [10,20,30,40]
    return render(request,"app2/3_inner.html",context=locals())

# @csrf_exempt  # 局部免除验证csrf_token
def login(request):
    if request.method == 'POST':
        print(request.POST.get('username'))
        return JsonResponse({'code':1,'msg':'success'})
    return render(request,'app2/4_login.html')


def extend(request):
    return render(request,'app2/5_inherent.html',context={'title':'过年了'})