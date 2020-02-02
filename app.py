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


@app.route("/get/<geoid_>")
def get_by_geoid(geoid_):
    try:
        median_income = MFI.query.filter_by(GEOID=geoid_).first()
        return jsonify(median_income.serialize())
    except Exception as e:
        return(str(e))


if __name__ == '__main__':
    app.run(debug=True)
