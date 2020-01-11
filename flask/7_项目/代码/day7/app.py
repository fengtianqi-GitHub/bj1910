from flask import Flask
from flask_script import Manager

from App.ext import db
from App.views import bbs

app = Flask(__name__)
app.config.from_pyfile('settings.py')

manager = Manager(app)

# 初始化db
db.init_app(app)

# 注册蓝图
app.register_blueprint(bbs)

if __name__ == '__main__':
    manager.run()
