# -*- coding: utf-8 -*-
# @File    : app.py
# 描述     ：
# @Time    : 2020/1/9 14:17
# @Author  : 
# @QQ      :  

from flask import Flask, request, redirect, url_for, abort, make_response, session, render_template
from flask_script import Manager

# 1.创建应用程序对象
from user import user

app = Flask(__name__)

# 1 应用配置
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@127.0.0.1:3306/bj1910"
# app.config['SECRET_KEY'] = "393934IO5L3K4MT98U(**(6789283RJ##@%543R"
# 从py文件加载配置
app.config.from_pyfile('settings.py')
# print(app.config)

manager = Manager(app)

@app.route('/',methods=['GET','POST'])
def index():
    print(request.args.get('hello'))
    print(request.form)
    print(request.values.get('hello'),request.values.get('name'))
    print("--"*100)
    print(request.headers)
    print()
    return render_template('index1.html',title='HHHHHH',name='admin' ,content="<h1>川普</h1>",num=3)

# 展示指定版块的帖子
@app.route('/list/<cid>',methods=['GET','POST'])
def list_post(cid):
    print(type(cid),cid)
    print(request.args)
    return "帖子列表"

@app.route('/show/<name>/<int:age>/')
def show(name,age):
    print(type(name),type(age))
    # return redirect('/')
    a= 100
    abort(400)
    # 由视图函数名生成请求路径
    print(url_for('list_post',cid=5,age=20))
    return redirect('/list/{}'.format(a))

@app.route('/response')
def custom_response():
    res = make_response("hello")
    res.headers['content-type']='plain'
    return res

app.register_blueprint(user)

if __name__ == '__main__':
    manager.run()