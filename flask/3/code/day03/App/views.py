from flask import Blueprint, render_template, g

first = Blueprint('first',__name__,url_prefix='/first')

@first.route('/index/')
def frirst_index():
    return render_template('index.html',title='haha',a=3,func=max)


@first.route('/nav/')
def navgate():
    return render_template('navigatebar.html')


@first.route('/global/')
def get_global():
    g.a = 10
    return  render_template("global.html")

import time
@first.context_processor
def get_current_time():
    def get_time(timeFormat="%b %d, %Y - %H:%M:%S"):
        return time.strftime(timeFormat)
    return dict(current_time=get_time,abc=10)