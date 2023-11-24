
from flask import Blueprint, jsonify, request, render_template
from flask_wtf import FlaskForm
from transport.models import User
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import Email, DataRequired

authentication_bp = Blueprint("authentication", __name__)

@authentication_bp.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        if login_form.validate():
            res = {
                "status": "success",
                "message": "Form valid"
            }
            return jsonify(res), 200
        else:
            return jsonify(login_form.errors), 400
    return render_template("login.html", form=login_form)


@authentication_bp.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if request.method == "POST":
        if register_form.validate():
            res = {
                "status": "success",
                "message": "Form valid"
            }
            return jsonify(res), 200
        else:
            return jsonify(register_form.errors), 400
    return render_template("register.html", form=register_form)

class LoginForm(FlaskForm):
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

