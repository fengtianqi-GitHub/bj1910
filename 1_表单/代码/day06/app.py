from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand


app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app) #实例例化ORM模型
migrate = Migrate(app,db) #实例例化迁移对象
manager = Manager(app)
manager.add_command('db',MigrateCommand) #添加迁移命令 别名为db


# 注册蓝图
from views import metoo
from user import user
app.register_blueprint(metoo)
app.register_blueprint(user)

if __name__ == '__main__':
    manager.run()
