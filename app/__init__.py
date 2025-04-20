from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')
    app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.game_routes import game_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(game_bp)

    return app
