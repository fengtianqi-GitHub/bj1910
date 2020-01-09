from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

#注册前台的用户模块
from App.user import user
app.register_blueprint(user)


if __name__ == '__main__':
    manager.run()
