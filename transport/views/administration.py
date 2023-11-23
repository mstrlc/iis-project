from flask import Blueprint, render_template
from transport.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired
from flask_login import current_user

administration_bp = Blueprint("administration", __name__)

@administration_bp.route("/users", methods=["GET", "POST"])
def users():
    users = User.query.all()
    return render_template("administration.html", users=users, current_user=current_user)

@administration_bp.route("/users/<int:user_id>", methods=["GET", "POST"])
def user(user_id):
    user = User.query.get(user_id)



class UserForm(FlaskForm):
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])