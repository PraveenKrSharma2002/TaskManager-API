from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['JWT_SECRET_KEY'] = 'supersecretkey'

    db.init_app(app)
    JWTManager(app)

    # IMPORT YAHAN KARNA HAI
    from .routes import main
    from .auth import auth

    # REGISTER YAHAN KARNA HAI
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app