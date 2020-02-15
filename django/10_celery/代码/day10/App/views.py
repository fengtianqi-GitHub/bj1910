from django.http import HttpResponse
from django.shortcuts import render
from App.tasks import intro,fib, send
# Create your views here.
def do_task(request):
    # 把任务放到队列中，其中任务的参数通过delay括号里参数传递的
    # intro.delay('李逸飞',22)  # 没有返回值的任务
    # 有返回值的任务
    # res = fib.delay(10)

    # 发送邮件
    send.delay('停课不停学','线上继续学','313728420@qq.com')
    return HttpResponse("异步任务")