import os

from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template, current_app, Blueprint
from transport.extensions import db, login_manager
from transport.views.home import home_bp
from transport.views.authentication import authentication_bp
from transport.views.administration import administration_bp
from transport.views.api.authentication import authentication_api_bp
from dotenv import load_dotenv
from transport.models import User

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["TESTING"] = True
    app.config["SESSION_COOKIE_SECURE"] = False

    app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'),
    )

    login_manager.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
        db.session.expunge_all()
        db.session.remove()

    app.register_blueprint(home_bp)
    app.register_blueprint(authentication_bp)
    app.register_blueprint(administration_bp)

    api_bp = Blueprint("api", __name__, url_prefix="/api")
    api_bp.register_blueprint(authentication_api_bp)
    app.register_blueprint(api_bp)

    return app

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

if __name__ == "__main__":
    app = create_app()
    app.run()