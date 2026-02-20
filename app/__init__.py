import os

from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import JWTManager

jwt = JWTManager()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    import os
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "dev-secret")
    jwt.init_app(app)

    db.init_app(app)

    from .auth import auth
    app.register_blueprint(auth)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
