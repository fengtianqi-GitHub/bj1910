from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from App.ext import db
from App.views import bbs
from App.models import *
from App.ext import cache


app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
cache.init_app(app)

#实例化迁移对象
Migrate(app=app,db=db)
manager = Manager(app)
manager.add_command('ok',MigrateCommand)

#注册蓝图
app.register_blueprint(bbs)

if __name__ == '__main__':
    manager.run()
