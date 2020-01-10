from flask import Flask, render_template, redirect, url_for, request, make_response
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

#注册蓝图
from views import tmp
from user import user
app.register_blueprint(tmp)
app.register_blueprint(user)


if __name__ == '__main__':
    manager.run()
