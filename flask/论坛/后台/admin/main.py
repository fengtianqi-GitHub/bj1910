import re

from flask import Blueprint, render_template, request, redirect, url_for, session
from App.models import Category,Posts,db,User

admin = Blueprint('admin',__name__,url_prefix='/admin')

# @admin.before_app_request
# def is_login():
#     if request.path.rstrip('/') == '/admin/login':
#         return None
#     if not session.get('username'):
#         return redirect(url_for('admin.login'))

@admin.route('/login/')
def login():
    return "登录先"


@admin.route('/')
def index():
    return  render_template('admin/admin_index.html')

# 版块管理
@admin.route('/category/',methods=["GET","POST"])
def category():
    # 大版块
    bigs = Category.query.filter(Category.parentid == 0).order_by(Category.orderby).all()
    # 小版块
    smalls = Category.query.filter(Category.parentid != 0).order_by(Category.orderby).all()
    # print(bigs, type(bigs[0]))
    if request.method == 'POST':
        for name in request.form:
            record = request.form.getlist(name)
            # 保存大版块信息
            for big in bigs:
                # print(big.compere,type(big.compere))
                if int(record[0]) == big.id:
                    # print(type(big.id), '---', type(record[1]))
                    big.classname = record[2]
                    big.orderby = record[1]
                    big.save()
                    # print(big)
                    break;
            # 保存小版块信息
            for small in smalls:
                if int(record[0]) == small.id:
                    small.orderby = record[1]
                    small.classname = record[2]
                    small.compere = record[3]
                    small.save()
                    break
    bigs.sort(key=lambda elem:elem.orderby)
    smalls.sort(key=lambda elem:elem.orderby)
    #get
    return render_template('admin/admin_category.html', **{
        'title': '版块管理',
        'bigs': bigs,
        'smalls': smalls
    })

@admin.route('/member/')
def member():
    return  render_template('admin/admin_member.html')
@admin.route('/detail/',methods=['GET','POST'])
def detail():
    if request.method == 'POST':
        data = request.form.getlist('tid')
        print(data)
        for tid in data:
            forum = Posts.query.get(tid)
            if forum.isdel == 0:
                forum.isdel = 1
                forum.save()
    page = int(request.args.get('page',1))
    data = db.session.query(Posts.id,Posts.title,User.username,Posts.replycount,Posts.hits,Posts.addtime,Category.classname).filter(User.id==Posts.user_id,Posts.category_id==Category.id,Posts.isdel==0).paginate(page,5)
    # print(data.items)
    # pagination = Posts.query.filter(Posts.isdel==0).paginate(page,15)
    return  render_template('admin/admin_detail.html',pagination=data)
    # return  "hello"


@admin.route('/site/')
def site():
    return  render_template('admin/admin_main.html')
@admin.route('/link/')
def link():
    return  render_template('admin/admin_link.html')

@admin.route('/lockip/')
def lockip():
    return  render_template('admin/admin_lock_ip.html')
@admin.route('/addcategory/')
def addcategory():
    return  render_template('admin/admin_category_add.html')

@admin.route('/deletepost/')
def deletepost():
    return  render_template('admin/admin_detail_del.html')
@admin.route('/reply/')
def reply():
    return  render_template('admin/admin_detail_hf.html')
@admin.route('/recyle/')
def recyle():
    return  render_template('admin/admin_detail_hf_del.html')

@admin.route("/adminstrate/")
def adminstrate():
    return "adminstrate"
@admin.route('/logout/')
def logout():
    return  '退出登录'

@admin.route('/dolink/')
def dolink():
    return  '退出登录'
