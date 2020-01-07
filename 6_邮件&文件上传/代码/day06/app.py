from flask import Flask
from flask_script import Manager

from ext import mail

app = Flask(__name__)
app.config.from_pyfile('settings.py')

mail.init_app(app)  # 初始化邮件发送对象

manager = Manager(app)


# 注册蓝图
from views import metoo
from user import user
app.register_blueprint(metoo)
app.register_blueprint(user)

if __name__ == '__main__':
    manager.run()
