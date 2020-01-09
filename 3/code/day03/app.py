from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__,
            template_folder='hello'  #定制模板目录
            )


#实例化Bootstrap对象，参数是app对象
Bootstrap(app)

#注册蓝图
from App.views import first
from App.user import user
app.register_blueprint(first)
app.register_blueprint(user)


manager = Manager(app)

@app.errorhandler(404)
def handle_404(err):
    return render_template('err.html',title='404',info="你请求的页面不存在")


if __name__ == '__main__':
    manager.run()
