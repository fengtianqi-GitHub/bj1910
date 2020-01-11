from flask import Flask, render_template, redirect, url_for, request, make_response
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def hello_world():
    return "hello world"
@app.route('/list/hello/')
@app.route('/list/hello/<int:num>/')
def show(num=1):
    print(type(num))
    return "参数"
@app.route('/who/')
def who():
    # return redirect('http://127.0.0.1:5000/list/hello/')
    # return redirect('/list/hello/')
    print(url_for('show',num=20))
    print(request.full_path)
    return redirect(url_for('show',num=20))

@app.route('/req')
def my_request():
    print(request.method)
    print(request.environ)
    # return "request"
    res = make_response("hello world")
    res.status_code = 200
    res.headers['Content-Type'] = 'text/html'
    return res



if __name__ == '__main__':
    manager.run()
