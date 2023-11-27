from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask_login import login_required, login_user, logout_user, current_user
from flask import current_app
from transport.models import User, Role

authentication_api_bp = Blueprint("authentication_api", __name__)


@authentication_api_bp.route("/login", methods=["POST"])
def login():
    # Already logged in
    if current_user.is_authenticated:
        res = {
            "status": "success",
            "message": "Already logged in",
        }
        return make_response(jsonify(res), 200)

    # Not logged in
    req = request.get_json()
    with current_app.app_context():
        user = User.query.filter_by(email=req.get("email")).first()
        # User does not exist in database
        if not user:
            res = {
                "status": "fail",
                "message": "User does not exist",
            }
            return make_response(jsonify(res), 401)
        # User exists in database but wrong password
        elif not user.verify_password(req.get("password")):
            res = {
                "status": "fail",
                "message": "Wrong password",
            }
            return make_response(jsonify(res), 401)
        # User exists in database and correct password
        else:
            login_user(user)
            res = {
                "status": "success",
                "message": "Logged in successfully",
            }
            return make_response(jsonify(res), 200)


@login_required
@authentication_api_bp.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    res = {
        "status": "success",
        "message": "Logged out successfully",
    }
    return make_response(jsonify(res), 200)


@authentication_api_bp.route("/register", methods=["POST"])
def register():
    # Already logged in
    if current_user.is_authenticated:
        res = {
            "status": "fail",
            "message": "Already logged in",
        }
        return make_response(jsonify(res), 401)

    # Not logged in
    req = request.get_json()
    with current_app.app_context():
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
            user_role = Role.query.filter_by(name="user").first()
            user = User(
                email=req.get("email"),
                firstname=req.get("firstname"),
                lastname=req.get("lastname"),
                password=req.get("password"),
                roles=[user_role],
            )
            user.save()
            res = {
                "status": "success",
                "message": "Registered successfully",
            }
            return make_response(jsonify(res), 201)