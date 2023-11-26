import datetime
from pyexpat import model
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask_login import login_required, login_user, logout_user, current_user
from flask import current_app
from transport.extensions import db
from transport.models import Stop, Vehicle, Line, LinesStops, Connection, Maintenance

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
        stop = Stop.query.filter_by(id = req.get("id")).first()
        stop.remove()
        res = {
            "status": "success",
            "message": "Removed stop successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/add_line", methods=["POST"])
def add_line():
    req = request.get_json()
    with current_app.app_context():
        line = Line()
        name = req.get("name")
        line.name = name
        line.save()
        res = {
            "status": "success",
            "message": "Add line successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/edit_line", methods=["POST"])
def edit_line():
    req = request.get_json()
    with current_app.app_context():
        line = Line.query.get(req.get("id"))
        name = req.get("name")
        line.name = name
        line.save()
        res = {
            "status": "success",
            "message": "Edit line successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/remove_line", methods=["POST"])
def remove_line():
    req = request.get_json()
    with current_app.app_context():
        line = Line.query.get(req.get("id"))
        line.remove()
        res = {
            "status": "success",
            "message": "Removed line successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/add_stop_to_line", methods=["POST"])
def add_stop_to_line():
    req = request.get_json()
    with current_app.app_context():
        line_stop = LinesStops()
        line_stop.line_id = req.get("id")
        line_stop.stop_id = req.get("stop_id")
        line_stop.save()
        res = {
            "status": "success",
            "message": "Add stop to line successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/remove_stop_from_line", methods=["POST"])
def remove_stop_from_line():
    req = request.get_json()
    with current_app.app_context():
        line_stop = LinesStops.query.filter_by(line_id = req.get("id"),stop_id = req.get("stop_id")).first()
        line_stop.remove()
        res = {
            "status": "success",
            "message": "Remove stop from line successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/add_vehicle", methods=["POST"])
def add_vehicle():
    req = request.get_json()
    with current_app.app_context():
        vehicle = Vehicle()
        name = req.get("name")
        type = req.get("type")
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
        vehicle = Vehicle.query.query.get(req.get("id"))
        vehicle.remove()
        res = {
            "status": "success",
            "message": "Removed vehicle successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/add_connection", methods=["POST"])
def add_connection():
    req = request.get_json()
    with current_app.app_context():
        connection = Connection()
        time = req.get("time")
        direction = req.get("direction")
        days_of_week = req.get("days_of_week")
        vehicle_id = req.get("vehicle_id")
        line_id = req.get("line_id")
        connection.time = time
        connection.direction = direction
        connection.days_of_week = days_of_week
        connection.vehicle_id = vehicle_id
        connection.line_id = line_id
        connection.save()
        res = {
            "status": "success",
            "message": "Add connection successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/edit_connection", methods=["POST"])
def edit_connection():
    req = request.get_json()
    with current_app.app_context():
        connection = Connection.query.get(req.get("id"))
        connection = Connection()
        time = req.get("time")
        direction = req.get("direction")
        days_of_week = req.get("days_of_week")
        vehicle_id = req.get("vehicle_id")
        line_id = req.get("line_id")
        connection.time = time
        connection.direction = direction
        connection.days_of_week = days_of_week
        connection.vehicle_id = vehicle_id
        connection.line_id = line_id
        connection.save()
        res = {
            "status": "success",
            "message": "Edit connection successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/remove_connection", methods=["POST"])
def remove_connection():
    req = request.get_json()
    with current_app.app_context():
        print(req.get("id"))
        connection = Connection.query.get(req.get("id"))
        connection.remove()
        res = {
            "status": "success",
            "message": "Removed connection successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/add_maintenance", methods=["POST"])
def add_maintenance():
    req = request.get_json()
    with current_app.app_context():
        maintenance = Maintenance()
        vehicle_id = req.get("vehicle_id")
        description = req.get("description")
        date = req.get("date")
        maintenance.vehicle_id = vehicle_id
        maintenance.date = date
        maintenance.description = description
        maintenance.save()
        res = {
            "status": "success",
            "message": "Add maintenance successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/edit_maintenance", methods=["POST"])
def edit_maintenance():
    req = request.get_json()
    with current_app.app_context():
        maintenance = Maintenance.query.get(req.get("id"))
        vehicle_id = req.get("vehicle_id")
        description = req.get("description")
        date = req.get("date")
        maintenance.vehicle_id = vehicle_id
        maintenance.date = date
        maintenance.description = description
        maintenance.save()
        res = {
            "status": "success",
            "message": "Edit maintenance successfully",
        }
        return make_response(jsonify(res), 200)

@management_api_bp.route("/remove_maintenance", methods=["POST"])
def remove_maintenance():
    req = request.get_json()
    with current_app.app_context():
        maintenance = Maintenance.query.get(req.get("id"))
        maintenance.remove()
        res = {
            "status": "success",
            "message": "Removed maintenance successfully",
        }
        return make_response(jsonify(res), 200)