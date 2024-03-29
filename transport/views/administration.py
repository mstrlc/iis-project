from flask import Blueprint, render_template
from transport.models import User, Role
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email
from flask_login import current_user, login_required
from flask import request, jsonify
from transport.views import roles_required

administration_bp = Blueprint("administration", __name__)

@administration_bp.route("/users", methods=["GET", "POST"])
@login_required
@roles_required(['admin'])
def users():
    users = User.query.all()
    return render_template("administration/users.html", users=users, current_user=current_user)

@administration_bp.route("/add_user", methods=["GET", "POST"])
@login_required
@roles_required(['admin'])
def add_user():
    roles = Role.query.all()
    user_form = UserForm()
    if request.method == "POST":
        if user_form.validate():
            res = {
                "status": "success",
                "message": "Form valid"
            }
            return jsonify(res), 200
        else:
            return jsonify(user_form.errors), 400
    return render_template("administration/add_user.html", form=user_form, current_user=current_user, roles=roles)

@administration_bp.route("/users/<int:user_id>", methods=["GET", "POST"])
@login_required
@roles_required(['admin'])
def edit_user(user_id):
    user = User.query.get(user_id)
    roles = Role.query.all()
    user_form = UserEditForm(obj=user)
    if request.method == "POST":
        if user_form.validate():
            res = {
                "status": "success",
                "message": "Form valid"
            }
            return jsonify(res), 200
        else:
            return jsonify(user_form.errors), 400
    return render_template("administration/edit_user.html", form=user_form, id=user.id, user=user, current_user=current_user, roles=roles)

class UserForm(FlaskForm):
    id = IntegerField("ID", render_kw={'readonly': True})
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

class UserEditForm(FlaskForm):
    id = IntegerField("ID", render_kw={'readonly': True})
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired(), Email()])
