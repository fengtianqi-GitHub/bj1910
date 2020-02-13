import os

from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.template import loader

from day08.settings import MEDIA_ROOT, EMAIL_HOST_USER


def do_upload(request):
    if request.method == 'POST':
        # 1 获取文件上传对象
        file_obj = request.FILES.get('photo')
        # if file_obj:
        #     # 2获取文件保存路径
        #     path = os.path.join(MEDIA_ROOT,file_obj.name)
        #     try:
        #         # 3将上传文件内容写入指定文件
        #         with open(path,'wb') as fp:
        #             # 如果文件大于2.5M
        #             if file_obj.multiple_chunks():
        #                 for chip in file_obj.chunk():
        #                     fp.write(chip)
        #             else:
        #                 fp.write(file_obj.read())
        #         return HttpResponse("上传成功")
        #     except :
        #         return HttpResponse("上传出错，请联系管理员")

        #使用自定义上传类测试
        from App01.uploadfile import Upload
        fupload = Upload(MEDIA_ROOT,ext=['jpg','jpeg','png'])
        res = fupload.load(file_obj)
        if isinstance(res,str):
            return HttpResponse(res)
        else:
            return HttpResponse("上传成功")

    return render(request,'app01/upload.html')


def send_one(request):
    send_mail("武汉加油","中国加油",EMAIL_HOST_USER,['xuexue715320@163.com','313728420@qq.com'])
    return HttpResponse("发送成功")


def send_many(request):
    # mail1 = ('我要发邮件1','我还要发邮件',EMAIL_HOST_USER,['xuexue715320@163.com'])
    # mail2 = ('我要发邮件2','我还要发邮件',EMAIL_HOST_USER,['313728420@qq.com'])
    # send_mass_mail((mail1,mail2))

    # 发送html邮件
    subject1, from_mail,to = ("女足",EMAIL_HOST_USER,['313728420@qq.com'])
    content = loader.get_template("app01/sport.html").render()
    obj = EmailMultiAlternatives(subject1,from_email=from_mail,to=to)
    obj.attach_alternative(content,'text/html')
    obj.send()
    return HttpResponse("发送成功")


def edit(request):
    if request.method == "POST":
        content = request.POST.get('content')
        return HttpResponse(content)
    return render(request,'app01/edit.html')