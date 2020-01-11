from flask import Flask

#创建应用实例
myapp = Flask(__name__)

#调试模式运行
myapp.config['DEBUG'] = True

#首页
@myapp.route('/')
def index():
    return "首页"

if __name__ == "__main__":
    myapp.run()
