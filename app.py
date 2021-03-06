import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import MFI


@app.route("/getall")
def get_all():
    try:
        median_incomes = MFI.query.all()
        return jsonify([e.serialize() for e in median_incomes])
    except Exception as e:
        return(str(e))


@app.route("/get/fips/<geoid_>")
def get_by_geoid(geoid_):
    try:
        median_income = MFI.query.filter_by(geoid=geoid_).first()
        return jsonify(median_income.serialize())
    except Exception as e:
        return(str(e))


@app.route("/get/state_code/<state_code_>")
def get_by_state_code(state_code_):
    try:
        median_income = MFI.query.filter_by(state_code=state_code_).all()
        return jsonify([i.serialize() for i in median_income])
    except Exception as e:
        return(str(e))


@app.route("/get/state_long/<state_name_>")
def get_by_state_long(state_name_):
    try:
        median_income = MFI.query.filter_by(state_name=state_name_).all()
        return jsonify([i.serialize() for i in median_income])
    except Exception as e:
        return(str(e))


@app.route("/get/state/<state_>")
def get_by_state(state_):
    try:
        median_income = MFI.query.filter_by(state=state_).all()
        return jsonify([i.serialize() for i in median_income])
    except Exception as e:
        return(str(e))


# add routes for specifying county name
@app.route("/get/state_long/<state_name_>/county/<string:county_>")
def get_by_state_long_and_county_name(state_name_, county_):
    try:
        county_long = '{} County'.format(county_)
        median_income = MFI.query.filter_by(state_name=state_name_).filter_by(county=county_long).first()
        return jsonify(median_income.serialize())
    except Exception as e:
        return(str(e))


@app.route("/get/state/<state_>/county/<string:county_>")
def get_by_state_and_county_name(state_, county_):
    try:
        county_long = '{} County'.format(county_)
        median_income = MFI.query.filter_by(
            state=state_).filter_by(county=county_long).first()
        return jsonify(median_income.serialize())
    except Exception as e:
        return(str(e))


if __name__ == '__main__':
    app.run(debug=True)
