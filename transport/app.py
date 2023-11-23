import os

from flask import Flask, render_template, current_app, Blueprint
from transport.extensions import db
from transport.views.home import home_bp
from transport.extensions import csrf
from transport.views.authentication import authentication_bp
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    csrf.init_app(app)

    db.init_app(app)
    
    app.register_blueprint(home_bp)
    app.register_blueprint(authentication_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()