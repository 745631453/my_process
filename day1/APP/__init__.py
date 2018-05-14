from flask import Flask
from APP.views import blue


def creste_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=blue)
    return app
