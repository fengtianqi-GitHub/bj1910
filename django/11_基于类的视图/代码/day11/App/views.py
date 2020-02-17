from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView,View,ListView,DetailView,CreateView

# Create your views here.
# FBV(function-based view)
from App.forms import UserForm
from App.models import User


class IndexView(TemplateView):
    pass

    # template_name = "App/index.html"
    # def get_context_data(self, **kwargs):
    #     # context = super().get_context_data(**kwargs)
    #     # context = {}
    #     # context['name'] = "千锋教育"
    #     return {'name':'千锋'}

# def index(request):
#     if request.method == "GET":
#         return HttpResponse("首页")
#     else:
#         return HttpResponse("首页")

# CBV
class RegisterView(View):
    def get(self,request):
        return render(request,"App/register.html")
    def post(self,request):
        # 业务处理
        print("1111111")
        return redirect(reverse("App:index"))
    def put(self,request):
        return HttpResponse("put")
    def head(self,request):
        return HttpResponse("head")
    def delete(self,request):
        return HttpResponse("delete")


class UserListView(ListView):
    # 指定查询结果集
    queryset = User.objects.all()
    # 指定模板文件名
    template_name = 'App/list.html'
    # 分页,每页10条记录
    paginate_by = 10


class UserDetailView(DetailView):
    template_name = 'App/detail.html'
    # 参数名称是uid，并且是主键
    pk_url_kwarg = 'uid'
    # 模板中所用参数名称
    context_object_name = 'user'
    # 查询所用模型
    model = User


class UserAddView(CreateView):
    template_name = 'App/add.html'
    # form_class = UserForm
    model = User
    # 提交成功后跳转的地址
    success_url = reverse_lazy("App:index")

    # 确定你用的是哪个表单
    def get_form(self, form_class=None):
        if self.request.method == "GET":
            return UserForm()
        else:
            return UserForm(self.request.POST)

    def form_valid(self, form):
        print(form.cleaned_data)
        # 保存数据
        user = User(**form.cleaned_data)
        user.save()
        return redirect(reverse("App:index"))

    def form_invalid(self, form):
        print(form)
        return super().form_invalid(form)


# 自定义装饰器
def wrapper(func):
    def inner(*args,**kwargs):
        print("*"*10)
        return func(*args,**kwargs)
    return inner

# 给类所有http的方法添加装饰器
# @method_decorator(wrapper,name='dispatch')
# @method_decorator(csrf_exempt,name='dispatch')
@method_decorator(csrf_exempt,name='dispatch')
class ExampleView(View):
    def get(self,request):
        print("get")
        return HttpResponse("get")

    # 为特定的方法添加装饰器
    # @method_decorator(wrapper)
    def post(self,request):
        print("post")
        return HttpResponse("post")