from flask import Blueprint

# 创建一个蓝图对象
#Blueprint(名称,模块名,路由前缀)
tmp = Blueprint('tmp',__name__,url_prefix='/tmp')

@tmp.route('/')
def index():
    return "tmp的首页"


@tmp.route('/hello/')
def hello():
    return "Hello World"

