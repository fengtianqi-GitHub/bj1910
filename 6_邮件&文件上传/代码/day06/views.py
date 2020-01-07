# -*- coding: utf-8 -*-
# @File    : views.py
# 描述     ：视图函数
# @Time    : 2020/1/6 9:38
# @Author  : 
# @QQ      :
import os

from flask import Blueprint, render_template, request, current_app, session

from tools import allowed_file

metoo = Blueprint('metoo',__name__,url_prefix='/app')

@metoo.route('/upload')  # 请求路径 /app/upload
def upload_file():
    return render_template("user.html")

# 文件上传处理
@metoo.route('/process',methods=['POST'])
def process_upload():
    print(request.files)
    # 获取文件上传对象
    upload_obj = request.files.get('picture')
    # print(upload_obj)
    if upload_obj:
        file_name = upload_obj.filename
        # current_app 代表应用程序对象，也就app模块中的app
        # print(current_app.config['UPLOAD_FOLDER'])
        # 拼接文件路径
        path = os.path.join(current_app.config['UPLOAD_FOLDER'],file_name)

        # 保存上传文件
        upload_obj.save(path)
        return render_template('picture.html',path='upload/'+file_name)
    return "文件不存在"

@metoo.route('/advance',methods=['POST'])
def advance_upload():
    upload_obj = request.files.get('picture')

    # 验证文件类型
    if upload_obj and allowed_file(upload_obj.filename):
        # 得到保存路径
        path = os.path.join(current_app.config.get('UPLOAD_FOLDER'),upload_obj.filename)
        upload_obj.save(path)
        size = os.path.getsize(path)
        if size > current_app.config.get('ALLOWED_MAX_SIZE'):
            os.remove(path)
            return "文件大小不符合要求"
    else:
        return "文件不存在或类型不符合要求"

    return "高级上传"

@metoo.route('/hello')
def hello():
    print(session.get('code'))
    return "Hello"