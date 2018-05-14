from flask import render_template
from flask import send_file
from flask import Blueprint

blue = Blueprint('first', __name__)


# 用来做业务逻辑的


# 路由
@blue.route('/')
def hello():
    # 视图函数
    return 'HELLO,world'


# 动态传入url参数
@blue.route('/he/<name>/')
def he(name):
    # 传入的name为字符串
    print(name)
    return 'hello %s' % name


# 修改后只能传入数字，否则报错
@blue.route('/hello/<int:name>/')
def hello_int(name):
    # 传入的name为整数
    print(name)
    return 'hello %s' % name


@blue.route('/index')
def inde():
    # return render_template('hello.html')
    return send_file('../templates/hello.html')


@blue.route('/float/<float:ff>')
def hello_float(ff):
    return 'hello %s' % ff


@blue.route('/uuid/<uuid:uu>')
def hello_uu(uu):
    return 'hello %s' % uu
