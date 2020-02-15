from datetime import datetime

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.cache import cache_page

# Create your views here.

# 缓存当前页面,缓存的是视图函数的渲染结果
@cache_page(30)
def home(request):
    current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current)
    return render(request,"index.html",locals())


# 页面局部缓存
def cahce_some_content(request):
    current1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request,'localcache.html',locals())

# 手动缓存
def custom_cache(request):

    # 1.从缓存中查询数据,如果有则返回
    html = cache.get('index')
    if html:
        print("缓存")
        return HttpResponse(html)
    # 2.如果缓存中没有，手动将数据缓存
    else:
        print("不走缓存")
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html = loader.get_template('index.html').render({'current':time})
        print(html)
        cache.set('index',html)
        return HttpResponse(html)


def do_log(request):
    print(1 / 0)
    return HttpResponse("日志操作")