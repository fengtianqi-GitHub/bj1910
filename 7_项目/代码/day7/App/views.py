# -*- coding: utf-8 -*-
# @File    : views.py
# 描述     ：
# @Time    : 2020/1/7 9:40
# @Author  : 
# @QQ      :  

from flask import Blueprint, render_template

from App.models import User

bbs = Blueprint('bbs',__name__)

@bbs.route('/')
def index():
    # data = User.query.filter().limit(10).all()
    # for user in data:
    #     print(user)
    return "首页"
# 多个路由对应一个视图函数
@bbs.route("/list/")
@bbs.route('/list/<int:page>/')
def list_user(page=1):
    # 得到分页对象
    pagenation = User.query.paginate(page,10)
    data = {
        'users':pagenation.items, # 当前页数据列表
        'current':pagenation.page, # 当前页码
        'per_page':pagenation.per_page, # 每页记录数
        'totals':pagenation.pages, # 总页数
        'next':pagenation.next_num, # 后一页页码
        'pre':pagenation.prev_num    # 前一页页码
    }
    return render_template('userlist.html',**data)

@bbs.route('/baidu/')
@bbs.route("/baidu/<int:page>/")
def show_users(page=1):
    # 得到分页对象
    pagenation = User.query.paginate(page, 10)

    # 计算页码列表
    if pagenation.page <= 5:
        # 如果总页数大于10，则显示前10页，否则显示1-总页数
        num = 10 if pagenation.pages >= 10 else pagenation.pages
        num = range(1,num+1)  # 页码范围
    else: # 当前页大于5
        last = pagenation.pages if (pagenation.page + 4)> pagenation.pages else (pagenation.page + 4)
        firt = pagenation.page - 5
        num = range(firt,last+1)



    data = {
        'users': pagenation.items,  # 当前页数据列表
        'current': pagenation.page,  # 当前页码
        'per_page': pagenation.per_page,  # 每页记录数
        'totals': pagenation.pages,  # 总页数
        'next': pagenation.next_num,  # 后一页页码
        'pre': pagenation.prev_num , # 前一页页码
        'iter_pages':num
    }
    return render_template('show.html', **data)
