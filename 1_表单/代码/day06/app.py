from flask import Flask
from flask_script import Manager

app = Flask(__name__)
app.config.from_pyfile('settings.py')
# print(app.config['BASEDIR'])
manager = Manager(app)


# 注册蓝图
from views import metoo
from user import user
app.register_blueprint(metoo)
app.register_blueprint(user)

if __name__ == '__main__':
    manager.run()
