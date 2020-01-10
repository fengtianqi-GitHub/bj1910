from flask import Flask, render_template, g
from flask_script import Manager


app = Flask(__name__)

# 模板的自动加载
app.config["TEMPLATES_AUTO_RELOAD"] = True
manager = Manager(app)

@app.route('/')
def hello_world():
    # html = render_template("index.html",title="我不是首页")
    # print(html,type(html))
    # return html
    #1 函数关键字参数传参
    # return render_template('index.html',title="搜狐",name='王大陆')
    #2.字典传参
    return render_template('index.html',**{'title':'首页',
                                           'name':'王大锤',
                                           'list1':[1,2,4,5],
                                           'dict1':{'hello':'you'}
                                           })
    #3 局部变量传参
    # title = '百度'
    # name = '王大傻'
    # return render_template('index.html',**locals())
    #全局变量g传参，在模板文件中可以直接使用g
    # g.title = '百度'
    # # g.name = 'hello'
    # return render_template('index.html')

def demo():
    return "哈哈"

@app.route('/filter/')
def my_filter():
    return render_template('filter.html',**{
        'world':'how are you',
        'content':"<h2>你好</h2>",
        'func':demo,
        'b':30
    })

@app.route('/flow/')
def flow():
    return render_template('flowcontroll.html',**{
        'hot':33,
        'students':[1,2,3,4,5,6]
    })

@app.route('/include')
def include_file():
    return render_template('intro.html',name="爱睡觉")

@app.route('/macro/')
def custom_marco():
    return render_template('marco.html')

@app.route('/base/')
def my_base():
    return render_template('common/Base.html')


@app.route('/index/')
def index1():
    return render_template('common/index.html',title='首页')

@app.route("/list/<cid>/")
def bbs_list(cid):
    return render_template('common/list.html',cid=cid)


if __name__ == '__main__':
    manager.run()
