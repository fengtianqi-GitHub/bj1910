from flask import Blueprint

# 创建一个蓝图对象
#Blueprint(名称,模块名,路由前缀)
user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/')
def user_index():
    return "首页"