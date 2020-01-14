from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def load_template(request):
    # # 获取模板对象
#     # template = loader.get_template("app2/load.html")
#     # print(template)
#     # list1 = [1,2,3,4]
#     # html = template.render(context={'list1':list1})
#     # print(html)
#     # return HttpResponse(html)
    return render(request,"app2/load.html",context={'list1':[1,2,3,4,5]})