from flask import Flask, session, render_template, redirect, url_for
from flask_script import Manager
from flask_session import Session
from redis import Redis

app = Flask(__name__)
#sessionid是根据secret_key生成了
app.config['SECRET_KEY'] = '48a4c553-2a00-456a-a1c9-9d64489bde00'
app.config['SESSION_PERMANENT'] = True
# 默认31天,可以是timedelta或int的数据
app.config['PERMANENT_SESSION_LIFETIME'] = 10000
# 指定session的保存方方式
app.config['SESSION_TYPE'] = 'redis'
# 指定redis连接实例例,默认127.0.0.1,6379端口口,0数据库
app.config['SESSION_REDIS'] = Redis(db=5)
#实例化Session对象
Session(app)

manager = Manager(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login/')
def login():
    session.permanent = True  #开启session的持久化
    app.permanent_session_lifetime = 3600  #秒数
    session['username'] = 'tom'
    return "设置session"

@app.route('/logout/')
def logout():
    # session.pop('username')  #清空指定的键值对
    session.clear()  #清空所有的session数据
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    manager.run()
