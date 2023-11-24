from flask import Blueprint, render_template
from transport.models import Stop
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email
from flask_login import current_user
from flask import request, jsonify

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

class StopForm(FlaskForm):
    id = IntegerField("ID", render_kw={'readonly': True})
    name = StringField("Stop Name", validators=[DataRequired()])
    latitude = StringField("Latitude", validators=[DataRequired()])
    longitude = StringField("Longitude", validators=[DataRequired()])
