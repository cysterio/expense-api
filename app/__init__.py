from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    app.secret_key = "supersecretkey"

    # Database config
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # JWT config
    app.config["JWT_SECRET_KEY"] = "this-is-a-very-secure-super-long-secret-key-12345"

    db.init_app(app)
    jwt.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app