from pyexpat import model
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask_login import login_required, login_user, logout_user, current_user
from flask import current_app
from transport.models import Stop, Vehicle

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
    
@management_api_bp.route('/add_vehicle')
def add_vehicle():
    req = request.get_json()
    with current_app.app_context():
        vehicle = Vehicle()
        name = req.get("name")
        type = req.get("tyoe")
        make = req.get("make")
        model = req.get("model")
        specs = req.get("specs")
        status = req.get("status")
        vehicle.name = name
        vehicle.type = type
        vehicle.make = make
        vehicle.model = model
        vehicle.specs = specs
        vehicle.status = status
        vehicle.save()
        res = {
            "status": "success",
            "message": "Add vehicle successfully",
        }
        return make_response(jsonify(res), 200)
    
@management_api_bp.route("/edit_vehicle", methods=["POST"])
def edit_vehicle():
    req = request.get_json()
    with current_app.app_context():
        vehicle = Vehicle.query.get(req.get("id"))
        vehicle = Vehicle()
        name = req.get("name")
        type = req.get("tyoe")
        make = req.get("make")
        model = req.get("model")
        specs = req.get("specs")
        status = req.get("status")
        vehicle.name = name
        vehicle.type = type
        vehicle.make = make
        vehicle.model = model
        vehicle.specs = specs
        vehicle.status = status
        vehicle.save()
        res = {
            "status": "success",
            "message": "Edit vehicle successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/remove_vehicle", methods=["POST"])
def remove_vehicle():
    req = request.get_json()
    with current_app.app_context():
        vehicle = Vehicle.query.get(req.get("id"))
        vehicle.deleted = True
        vehicle.save()
        res = {
            "status": "success",
            "message": "Removed vehicle successfully",
        }
        return make_response(jsonify(res), 200)