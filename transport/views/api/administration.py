from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask_login import login_required, login_user, logout_user, current_user
from flask import current_app
from transport.models import User

administration_api_bp = Blueprint("administration_api", __name__)


@administration_api_bp.route("/edit_user", methods=["POST"])
def edit_user():
    req = request.get_json()
    with current_app.app_context():
        user = User.query.get(req.get("id"))
        firstname = req.get("firstname")
        lastname = req.get("lastname")
        email = req.get("email")
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
        user.save()
        res = {
            "status": "success",
            "message": "Edited user successfully",
        }
        return make_response(jsonify(res), 200)