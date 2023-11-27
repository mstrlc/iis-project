import os

from flask_wtf.csrf import CSRFProtect
from flask import Flask, render_template, current_app, Blueprint
from transport.extensions import db, login_manager
from transport.views.home import home_bp
import transport.views.authentication as authentication
import transport.views.administration as administration
import transport.views.management as management
import transport.views.api.authentication as authentication_api
import transport.views.api.administration as administration_api
import transport.views.api.management as management_api
from dotenv import load_dotenv
from transport.models import User
import transport.sample_data as sd

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    # if you changed models, set this to True
    app.config["MODELS_CHANGED"] = False 
    # if you want to insert sample data, set this to True   
    app.config["SAMPLE_DATA"] = True
    app.config["SESSION_COOKIE_SECURE"] = False

    app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'),
    )

    login_manager.init_app(app)
    db.init_app(app)
    with app.app_context():

        if app.config["SAMPLE_DATA"] == True:
            models_changed(app)
        db.create_all()

        db.session.commit()
        db.session.expunge_all()
        db.session.remove()

    app.register_blueprint(home_bp)
    app.register_blueprint(authentication.authentication_bp)
    app.register_blueprint(management.management_bp)
    app.register_blueprint(administration.administration_bp)

    api_bp = Blueprint("api", __name__, url_prefix="/api")
    api_bp.register_blueprint(authentication_api.authentication_api_bp)
    api_bp.register_blueprint(administration_api.administration_api_bp)
    api_bp.register_blueprint(management_api.management_api_bp)
    app.register_blueprint(api_bp)

    return app


def models_changed(app):
    with app.app_context():
        if app.config["MODELS_CHANGED"] == True:
            db.drop_all()
        db.create_all()
        sd.insert_sample_lines()
        sd.insert_sample_stops()
        sd.insert_sample_vehicles()
        sd.insert_sample_roles()
        sd.insert_sample_users()
        sd.insert_sample_connections()



@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

if __name__ == "__main__":
    app = create_app()
    app.run()