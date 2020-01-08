# -*- coding: utf-8 -*-
# @File    : views.py
# 描述     ：
# @Time    : 2020/1/7 14:33
# @Author  : 
# @QQ      :  

from flask import Blueprint, render_template

from App.models import Category

bbs = Blueprint('bbs',__name__)

@bbs.route('/')
def index():
    # 查询大板块数据
    big_category = Category.query.filter(Category.parentid==0).all()

    return render_template("index/index.html",big_category=big_category)