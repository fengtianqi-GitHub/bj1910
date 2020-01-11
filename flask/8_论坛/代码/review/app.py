from flask import Flask, request
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from sqlalchemy import func, or_

from extensions import db
from models import User, Post

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:123@127.0.0.1:3306/test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

db.init_app(app)

@app.route('/')

# 在用户请求获得处理之前拦截用户请求
@app.before_request
def prevent():
    print(request.remote_addr,request.path)
    return "kkkkk"
def hello_world():
    # user = User(username='tom', password='123')
    # user.save()

    # 查询
    # data = User.query.get(200)
    # data = User.query.filter(User.id==200).first()
    # data = User.query.with_entities(User.sex).distinct().all()
    # data = User.query.order_by(User.id).limit(1).all()
    # data = User.query.order_by(User.id).limit(1).all()
    # data = db.session.query(func.max(User.id).label('num')).scalar()
    # select sex,count(*) from bbs_user group by sex
    # num = func.count(User.sex)
    # data = db.session.query(User.sex,num).group_by(User.sex).having(num>0).all()
    # data = User.query.filter(or_(User.sex==2,User.id<210)).all()
    # data = db.session.query(User,Post).filter(User.id==Post.authorid).all()
    # print(globals())
    # 连接查询
    # data = db.session.query(User,Post).filter(User.id==Post.authorid).all()
    # 原生sql
    # sql = "select * from bbs_user"
    # cursor = db.session.execute(sql)
    # data = cursor.fetchall()
    #
    # print(data,type(data))


    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
