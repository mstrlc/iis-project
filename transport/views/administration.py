from flask import Blueprint, render_template
from transport.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired
from flask_login import current_user
from flask import request, jsonify

administration_bp = Blueprint("administration", __name__)

@administration_bp.route("/users", methods=["GET", "POST"])
def users():
    users = User.query.all()
    return render_template("administration/users.html", users=users, current_user=current_user)

@administration_bp.route("/users/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = User.query.get(user_id)
    user_form = UserForm(obj=user)
    if request.method == "POST":
        if user_form.validate():
            res = {
                "status": "success",
                "message": "Form valid"
            }
            return jsonify(res), 200
        else:
            return jsonify(user_form.errors), 400
    return render_template("administration/edit_user.html", form=user_form, id=user.id, user=user, current_user=current_user)

class UserForm(FlaskForm):
    id = IntegerField("ID", render_kw={'readonly': True})
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])