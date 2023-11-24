from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask_login import login_required, login_user, logout_user, current_user
from flask import current_app
from transport.models import Stop

management_api_bp = Blueprint("management_api", __name__)

@management_api_bp.route("/add_stop", methods=["POST"])
def add_stop():
    req = request.get_json()
    with current_app.app_context():
        stop = Stop()
        name = req.get("name")
        latitude = req.get("latitude")
        longitude = req.get("longitude")
        stop.name = name
        stop.latitude = latitude
        stop.longitude = longitude
        stop.save()
        res = {
            "status": "success",
            "message": "Add stop successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/edit_stop", methods=["POST"])
def edit_stop():
    req = request.get_json()
    with current_app.app_context():
        stop = Stop.query.get(req.get("id"))
        name = req.get("name")
        latitude = req.get("latitude")
        longitude = req.get("longitude")
        stop.name = name
        stop.latitude = latitude
        stop.longitude = longitude
        stop.save()
        res = {
            "status": "success",
            "message": "Edit stop successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/remove_stop", methods=["POST"])
def remove_stop():
    req = request.get_json()
    with current_app.app_context():
        stop = Stop.query.get(req.get("id"))
        stop.deleted = True
        stop.save()
        res = {
            "status": "success",
            "message": "Removed stop successfully",
        }
        return make_response(jsonify(res), 200)
