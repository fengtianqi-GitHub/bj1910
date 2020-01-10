from flask import Flask, redirect,  make_response
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route("/")
def index():
    # return "first page"
    return "first page",300
@app.route('/response/')
def my_response():
    tmp = make_response("自定义响应对象")
    tmp.status_code = 404  # 状态吗
    tmp.headers['haha'] = "hahah"  #定制响应头信息
    return tmp




if __name__ == '__main__':
    manager.run()

