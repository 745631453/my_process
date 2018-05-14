from flask_script import Manager
from APP import creste_app

# 初始化，--name--代表主模块名或者包
# app = Flask(__name__)
blue = creste_app()
manager = Manager(app=blue)


if __name__ == '__main__':
    # 启动
    # app.run(debug=True)
    manager.run()
