from App.ext import db
class Student(db.Model):
    sno = db.Column(db.Integer,primary_key=True,autoincrement=True)
    sname = db.Column(db.String(30))
    #uselist=False表示student和detail是一对一关系
    detail = db.relationship('Detail',backref='stu',uselist=False)
    courses = db.relationship('Course',secondary='sc',backref='students')
    __tablename__ = 'student'


class Detail(db.Model):
    did = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nickyname = db.Column(db.String(60))
    sno = db.Column(db.Integer,db.ForeignKey("student.sno"),unique=True)
    __tablename__ = 'detail'


class Course(db.Model):
    cno = db.Column(db.Integer,primary_key=True,autoincrement=True)
    cname = db.Column(db.String(60))
    __tablename__ = 'course'

# 中间表
sc = db.Table('sc',
              db.Column('sno',db.Integer,db.ForeignKey('student.sno')),
              db.Column('cno',db.Integer,db.ForeignKey('course.cno'))
              )