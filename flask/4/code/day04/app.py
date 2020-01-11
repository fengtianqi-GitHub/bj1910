from flask import Flask
from flask_script import Manager

from App.views import bbs
from ext import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123@127.0.0.1:3306/day05"
# 不实时跟踪数据库发生的变化
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)

#初始化
db.init_app(app)


#注册蓝图
app.register_blueprint(bbs)


if __name__ == '__main__':
    manager.run()
