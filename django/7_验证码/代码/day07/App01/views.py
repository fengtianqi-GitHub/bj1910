from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App01.forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('username'))
            print(form.cleaned_data)
            return HttpResponse("首页")
        else:
            print(form.errors)
            return render(request, "app01/register.html",locals())
    return render(request,"app01/register.html")


def verify(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        # 验证
        if form.is_valid():
            return HttpResponse("验证通过")
        else:
            return render(request, 'app01/login.html', locals())

    form = LoginForm()
    return render(request,'app01/login.html',locals())