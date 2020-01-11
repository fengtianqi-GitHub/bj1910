from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 数据库链接配置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@127.0.0.1:3306/day04"
# 开启自动提交
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 实例化sqlalchemy对象
db = SQLAlchemy(app)
# 实例化迁移对象
Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# db.Model是所有模型类的父类，自己的模型类必须继承Model
class Stuent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sno = db.Column(db.String(11), unique=True)
    sname = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, default=0)
    # 指定表名
    __tablename__ = 'student'


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
