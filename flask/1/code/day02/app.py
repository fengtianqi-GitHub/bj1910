from flask import Flask, render_template, request, redirect
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

# 无参路由，请求路径中不包括参数
# 路由规则必须以正斜线开头
@app.route('/')
def hello_world():
    return 'Hello World!'
# 路由规则如果以/结尾，则请求路径最后可以带斜线或不带斜线，但不带斜线，会有一次重定向
# 推荐路由规则末尾添加一个/
@app.route('/hello')
def howareyou():
    return  "How are you"

# 带参数的路由
# 路由规则中有几个参数，视图函数就要有几个参数，并且严格按照从左向右一一匹配
# 函数参数名称要和路由中的名字一样
@app.route('/index/')
@app.route('/index/<bid>/')
def index(bid='1'):
    return bid

# 视图函数不能重名
# @app.route('/index/')
# def index(bid):
#     return bid

@app.route("/student/<sno>/<sname>/<sage>/")
def who(sno,sname,sage):
    print(sno,sname,sage)
    return "我也不知道你是谁"

#参数类型
# @app.route('/list/<tid>/')  #参数类型默认是str
# @app.route('/list/<int:tid>/')  #参数类型是int
# @app.route('/list/<float:tid>/')  #参数类型是float
@app.route('/list/<path:tid>/')  #参数类型是path,path将参数中/看作普通字符
def show_list(tid):
    print(type(tid))
    print(tid)
    return "参数类型"

#请求方法
@app.route("/login/",methods=['GET','POST'])
def login():
    #values既可以获取get也可以获取post参数
    print(request.values)
    if request.method == 'POST':
        # print(request.form)
        # print(request.form.get('username'))
        # print(request.form.getlist('hobby'))
        return redirect('/')
    else:
        # print(request.values.get('username'))
        # print(request.url)
        # print(request.base_url)
        # print(request.host_url)
        # print(request.host)
        # print("请求路径：",request.path)
        # print("请求路径+参数：",request.full_path)
        # print("请求方法：",request.method)
        # print("客户端ip地址：",request.remote_addr)
        # print("get传参（？后的参数）：",request.args)
        # # args是get参数字典，使用args.get("键")获取单个值
        # print(request.args.get('name'))
        # print(request.args.get('age'))
        #使用args.getlist("键"),获取一个键多个值
        # print(request.args.getlist('age'))
        # print(request.args.get('username'))

        return render_template("login.html")

@app.route('/params')
def get_param():
    # 请求头信息
    # print(request.headers)
    # 请求相关的环境变量
    print(request.environ)
    return "获取参数"


if __name__ == '__main__':
    # app.run()
    manager.run()