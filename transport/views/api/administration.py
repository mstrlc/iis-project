from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask_login import login_required, login_user, logout_user, current_user
from flask import current_app
from transport.models import User, Role

administration_api_bp = Blueprint("administration_api", __name__)

@administration_api_bp.route("/add_user", methods=["POST"])
def add_user():
    req = request.get_json()
    with current_app.app_context():
        firstname = req.get("firstname")
        lastname = req.get("lastname")
        email = req.get("email")
        password = req.get("password")
        role_id = req.get("role")
        # Try to find user in database
        user = User.query.filter_by(email=req.get("email")).first()
        # User does not exist in database
        if user:
            res = {
                "status": "fail",
                "message": "User already exists",
            }
            return make_response(jsonify(res), 401)
        # New user
        else:
            user_role = Role.query.filter_by(id="role_id").first()
            user = User(
                email=req.get("email"),
                firstname=req.get("firstname"),
                lastname=req.get("lastname"),
                password=req.get("password"),
                role=user_role,
            )
            user.save()
            res = {
                "status": "success",
                "message": "Registered successfully",
            }
            return make_response(jsonify(res), 201)


        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user and existing_user.email == email:
            res = {
                "status": "fail",
                "message": "Email already exists",
            }
            return make_response(jsonify(res), 422)
        # Email does not exist, create new user
        role = Role.query.filter_by(id=role_id).first()
        user = User(firstname=firstname, lastname=lastname, email=email, password=password, roles=[role])
        user.save()
        res = {
            "status": "success",
            "message": "Added user successfully",
        }
        return make_response(jsonify(res), 200)

@administration_api_bp.route("/edit_user", methods=["POST"])
def edit_user():
    req = request.get_json()
    with current_app.app_context():
        user = User.query.get(req.get("id"))
        firstname = req.get("firstname")
        lastname = req.get("lastname")
        email = req.get("email")
        role_id = req.get("role")
        # Check if email was changed
        if user.email != email:
            # Check if email already exists
            existing_user = User.query.filter_by(email=email).first()
            if existing_user and existing_user.email == email:
                res = {
                    "status": "fail",
                    "message": "Email already exists",
                }
                return make_response(jsonify(res), 422)
        # Email does not exist, edit user
        user.firstname = firstname
        user.lastname = lastname
        user.email = email
        role = Role.query.filter_by(id=role_id).first()
        user.roles = [role]
        user.save()
        res = {
            "status": "success",
            "message": "Edited user successfully",
        }
        return make_response(jsonify(res), 200)

@administration_api_bp.route("/remove_user", methods=["POST"])
def remove_user():
    req = request.get_json()
    with current_app.app_context():
        user = User.query.get(req.get("id"))
        user.remove()
        res = {
            "status": "success",
            "message": "Removed user successfully",
        }
        return make_response(jsonify(res), 200)
