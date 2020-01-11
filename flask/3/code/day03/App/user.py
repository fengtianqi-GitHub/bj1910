from flask import Blueprint, render_template, request, redirect, url_for, make_response

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/login/')
def user_login():
    return  render_template('App/index.html')

@user.route('/dologin/',methods=['GET','POST'])
def user_dologin():
    # 获取提交参数
    username = request.form.get('username')
    password = request.form.get('password')

    #验证用户名和密码是否正确
    if username == 'admin' and password == '123':
        #将登陆信息写入cookie
        #跳转指定页面
        # response = make_response("<html><head><meta http-equiv='refresh' content='0;url=/user/'></head></html>")
        response = make_response("<script>window.location.href='/user/login/'</script>")
        # 刷新本页面
        # response = make_response(render_template('App/index.html'))
        response.set_cookie('username',username,max_age=3*24*3600)

        #验证正确跳转首页
        return response
    #验证错误，重新验证
    return redirect(url_for('user.user_login'))

@user.route('/')
def index():
    return "首页"

@user.route('/logout/')
def user_logout():
    res = make_response("<script>window.location.href='/user/login/'</script>")
    # res = make_response()
    res.delete_cookie('username')
    return res