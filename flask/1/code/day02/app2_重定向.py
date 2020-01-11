from flask import Flask, redirect, url_for, abort, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return "首页"

@app.route('/login/')
def login():
    # 根据视图函数名获取函数所对应请求路径
    #_external如果设置为True，可以得到完整的url
    print(url_for('register',_external=True))

    #redirect参数是请求路径
    # return redirect('/')
    # return redirect(url_for('register'))
    # return redirect('/show/tom/34/')
    name = '哈哈'
    age = 20
    print(url_for('show',name=name,age=age))
    return redirect(url_for('show',name=name,age=age,a=30,b=90.5))
@app.route("/register/")
def register():
    return "注册"

@app.route("/show/<name>/<age>/")
def show(name,age):
    return name + "---" + age

@app.route('/error/')
def handle_error():
    abort(500)
    print("hhhh")

# 错误捕获，定制自己的错误页面
@app.errorhandler(500)
def catch_500(err):
    print(err)
    return render_template('500.html',err=err)

@app.errorhandler(404)
def catch_404(err):
    print(err)
    return render_template('404.html')

if __name__ == '__main__':
    manager.run()

