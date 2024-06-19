from flask import Flask
from .routes import users

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(users.user_bp)

    return app

