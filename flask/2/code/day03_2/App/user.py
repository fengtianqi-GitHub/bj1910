from flask import Blueprint

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/register/')
def register():
    return "用户注册"
@user.route("/login/")
def login():
    return "用户登录"