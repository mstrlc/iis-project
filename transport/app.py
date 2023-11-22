import os

from flask import Flask, render_template, current_app, Blueprint
from transport.extensions import db
from transport.views.home import home_bp
from dotenv import load_dotenv

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

    db.init_app(app)

    app.register_blueprint(home_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()