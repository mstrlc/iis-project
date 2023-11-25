from flask import Blueprint, render_template
from transport.models import Stop, Vehicle, Line, lines_stops
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email
from flask_login import current_user
from flask import request, jsonify
from wtforms import ValidationError
import re

management_bp = Blueprint("management", __name__)

@management_bp.route("/stops", methods=["GET", "POST"])
def stops():
    stops = Stop.query.all()
    return render_template("management/stops.html", stops=stops)

@management_bp.route("/stops/add", methods=["GET", "POST"])
def add_stop():
    stop_form = StopForm()
    if request.method == "POST":
        if stop_form.validate():
            res = {
                "status": "success",
                "message": "Form valid"
            }
            return jsonify(res), 200
        else:
            return jsonify(stop_form.errors), 400
    return render_template("management/add_stop.html", form=stop_form)

@management_bp.route("/stops/<int:stop_id>", methods=["GET", "POST"])
def edit_stop(stop_id):
    stop = Stop.query.get(stop_id)
    stop_form = StopForm(obj=stop)
    if request.method == "POST":
        if stop_form.validate():
            res = {
                "status": "success",
                "message": "Form valid"
            }
            return jsonify(res), 200
        else:
            return jsonify(stop_form.errors), 400
    return render_template("management/edit_stop.html", form=stop_form, id=stop.id, stop=stop)

@management_bp.route("/lines", methods=["GET", "POST"])
def lines():
    lines = Line.query.all()
    return render_template("management/lines.html", lines=lines)

@management_bp.route("/lines/add", methods=["GET", "POST"])
def add_line():
    line_form = LineForm()
    if request.method == "POST":
        if line_form.validate():
            res = {
                "status": "success",
                "message": "Form valid"
            }
            return jsonify(res), 200
        else:
            return jsonify(line_form.errors), 400
    return render_template("management/add_line.html", form=line_form)

@management_bp.route("/lines/<int:line_id>", methods=["GET", "POST"])
def edit_line(line_id):
    line = Line.query.get(line_id)
    stops = Stop.query.all()
    line_stops = line.line_stops
    line_form = LineForm(obj=line)
    if request.method == "POST":
        if line_form.validate():
            res = {
                "status": "success",
                "message": "Form valid"
            }
            return jsonify(res), 200
        else:
            return jsonify(line.errors), 400
    return render_template("management/edit_line.html", form=line_form, id=line.id, line=line, stops=stops, line_stops=line_stops)

@management_bp.route("/vehicles", methods=["GET", "POST"])
def vehicles():
    vehicles = Vehicle.query.all()
    return render_template("management/vehicles.html", vehicles=vehicles)

@management_bp.route("/vehicles/add", methods=["GET", "POST"])
def add_vehicle():
    vehicle_form = VehicleForm()
    if request.method == "POST":
        if vehicle_form.validate():
            res = {
                "status": "success",
                "message": "Form valid"
            }
            return jsonify(res), 200
        else:
            return jsonify(vehicle_form.errors), 400
    return render_template("management/add_vehicle.html", form=vehicle_form)

@management_bp.route("/vehicles/<int:vehicle_id>", methods=["GET", "POST"])
def edit_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    vehicle_form = VehicleForm(obj=vehicle)
    if request.method == "POST":
        if vehicle_form.validate():
            res = {
                "status": "success",
                "message": "Form valid"
            }
            return jsonify(res), 200
        else:
            return jsonify(vehicle_form.errors), 400
    return render_template("management/edit_vehicle.html", form=vehicle_form, id=vehicle.id, vehicle=vehicle)

class StopForm(FlaskForm):
    id = IntegerField("ID", render_kw={'readonly': True})
    name = StringField("Stop Name", validators=[DataRequired()])
    latitude = StringField("Latitude", validators=[DataRequired()])
    longitude = StringField("Longitude", validators=[DataRequired()])

    def validate_latitude(self, latitude):
        # 49.2277139N
        if not re.match(r"^\d+\.\d+[NS]$", latitude.data):
            raise ValidationError("Invalid latitude format, should be WGS84 (degrees)")

    def validate_longitude(self, longitude):
        # 123.0074463W
        if not re.match(r"^\d+\.\d+[EW]$", longitude.data):
            raise ValidationError("Invalid longitude format, should be WGS84 (degrees)")

class LineForm(FlaskForm):
    id = IntegerField("ID", render_kw={'readonly': True})
    name = StringField("Line Name", validators=[DataRequired()])

class VehicleForm(FlaskForm):
    id = IntegerField("ID", render_kw={'readonly': True})
    name = StringField("Vehicle Name", validators=[DataRequired()])
    type = StringField("Vehicle type", validators=[DataRequired()])
    make = StringField("Make", validators=[DataRequired()])
    model = StringField("Model", validators=[DataRequired()])
    specs = StringField("Technical specs", validators=[DataRequired()])
    status = StringField("Vehicle status", validators=[DataRequired()])