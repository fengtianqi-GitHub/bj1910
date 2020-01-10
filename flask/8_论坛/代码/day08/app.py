from flask import Flask, render_template
from flask_script import Manager
from forms import RegisterForm
from extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://python:123@47.88.225.157:3306/bj1910"
app.config["SQLALCHEMY_TRACK_MODIFICAIONS"] = False
app.config["SECRET_KEY"] = "237849234JK93490230490257690%$^7M<<,,.JJI"

db.init_app(app)
manager = Manager(app)
@app.route('/')
def hello_world():
    form = RegisterForm()
    return render_template('register.html',form=form)

@app.route("/register",methods=['POST'])
def register():
    form = RegisterForm()
    # validate_on_submit验证提交的数据，验证通过返回True，否则返回False
    if form.validate_on_submit():
        # 获取验证后的数据
        print(form.username.data)
        print(form.password.data)
        return "验证通过"
    else:
        return render_template('register.html',form=form)

if __name__ == '__main__':
    manager.run()
