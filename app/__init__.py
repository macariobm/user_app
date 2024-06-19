from flask import Flask
from app.routes import users
from app.database import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(users.user_bp)

    db.init_app(app)

    return app




