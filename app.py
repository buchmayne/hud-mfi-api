import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'].replace(
    "://", "ql://", 1)
db = SQLAlchemy(app)


class MFI(db.Model):
    __tablename__ = 'mfi'

    geoid = db.Column(db.String(), primary_key=True)
    state = db.Column(db.String())
    state_code = db.Column(db.String())
    state_name = db.Column(db.String())
    county_code = db.Column(db.String())
    county = db.Column(db.String())
    mfi_2000 = db.Column(db.Integer())
    mfi_2001 = db.Column(db.Integer())
    mfi_2002 = db.Column(db.Integer())
    mfi_2003 = db.Column(db.Integer())
    mfi_2004 = db.Column(db.Integer())
    mfi_2005 = db.Column(db.Integer())
    mfi_2006 = db.Column(db.Integer())
    mfi_2007 = db.Column(db.Integer())
    mfi_2008 = db.Column(db.Integer())
    mfi_2009 = db.Column(db.Integer())
    mfi_2010 = db.Column(db.Integer())
    mfi_2011 = db.Column(db.Integer())
    mfi_2012 = db.Column(db.Integer())
    mfi_2013 = db.Column(db.Integer())
    mfi_2014 = db.Column(db.Integer())
    mfi_2015 = db.Column(db.Integer())
    mfi_2016 = db.Column(db.Integer())
    mfi_2017 = db.Column(db.Integer())
    mfi_2018 = db.Column(db.Integer())
    mfi_2019 = db.Column(db.Integer())
    mfi_2020 = db.Column(db.Integer())
    mfi_2021 = db.Column(db.Integer())

    def __init__(
        self,
        geoid,
        state,
        state_code,
        state_name,
        county_code,
        county,
        mfi_2000,
        mfi_2001,
        mfi_2002,
        mfi_2003,
        mfi_2004,
        mfi_2005,
        mfi_2006,
        mfi_2007,
        mfi_2008,
        mfi_2009,
        mfi_2010,
        mfi_2011,
        mfi_2012,
        mfi_2013,
        mfi_2014,
        mfi_2015,
        mfi_2016,
        mfi_2017,
        mfi_2018,
        mfi_2019,
        mfi_2020,
        mfi_2021
    ):
        self.geoid = geoid
        self.state = state
        self.state_code = state_code
        self.state_name = state_name
        self.county_code = county_code
        self.county = county
        self.mfi_2000 = mfi_2000
        self.mfi_2001 = mfi_2001
        self.mfi_2002 = mfi_2002
        self.mfi_2003 = mfi_2003
        self.mfi_2004 = mfi_2004
        self.mfi_2005 = mfi_2005
        self.mfi_2006 = mfi_2006
        self.mfi_2007 = mfi_2007
        self.mfi_2008 = mfi_2008
        self.mfi_2009 = mfi_2009
        self.mfi_2010 = mfi_2010
        self.mfi_2011 = mfi_2011
        self.mfi_2012 = mfi_2012
        self.mfi_2013 = mfi_2013
        self.mfi_2014 = mfi_2014
        self.mfi_2015 = mfi_2015
        self.mfi_2016 = mfi_2016
        self.mfi_2017 = mfi_2017
        self.mfi_2018 = mfi_2018
        self.mfi_2019 = mfi_2019
        self.mfi_2020 = mfi_2020
        self.mfi_2021 = mfi_2021

    def __repr__(self):
        return '<geoid {}>'.format(self.geoid)

    def serialize(self):
        return {
            'geoid': self.geoid,
            'state': self.state,
            'state_code': self.state_code,
            'state_name': self.state_name,
            'county_code': self.county_code,
            'county': self.county,
            'mfi_2000': self.mfi_2000,
            'mfi_2001': self.mfi_2001,
            'mfi_2002': self.mfi_2002,
            'mfi_2003': self.mfi_2003,
            'mfi_2004': self.mfi_2004,
            'mfi_2005': self.mfi_2005,
            'mfi_2006': self.mfi_2006,
            'mfi_2007': self.mfi_2007,
            'mfi_2008': self.mfi_2008,
            'mfi_2009': self.mfi_2009,
            'mfi_2010': self.mfi_2010,
            'mfi_2011': self.mfi_2011,
            'mfi_2012': self.mfi_2012,
            'mfi_2013': self.mfi_2013,
            'mfi_2014': self.mfi_2014,
            'mfi_2015': self.mfi_2015,
            'mfi_2016': self.mfi_2016,
            'mfi_2017': self.mfi_2017,
            'mfi_2018': self.mfi_2018,
            'mfi_2019': self.mfi_2019,
            'mfi_2020': self.mfi_2020,
            'mfi_2021': self.mfi_2021
        }


@app.route('/', methods=['GET'])
def home():
    home_html = """<h1 id="hud-mfi-api-documentation">HUD-MFI-API Documentation</h1>
    <p>The Department of Housing and Urban Development (HUD) sets income limits that determine eligibility for assisted housing programs including the Public Housing, Section 8 project-based, Section 8 Housing Choice Voucher, Section 202 housing for the elderly, and Section 811 housing for persons with disabilities programs. HUD develops income limits based on Median Family Income estimates and Fair Market Rent area definitions for each metropolitan area, parts of some metropolitan areas, and each non-metropolitan county.</p>
    <p>HUD also provides an API (Application Programming Interface) that makes it easy to access median family income estimates for each U.S. county. However, the HUD API only provides access to the most recent year&#39;s median family income estimate. Often it is informative to analyze housing affordability through time which requires access to HUD&#39;s historical median family income estimates.</p>
    <p>The following documentation outlines the usage of a custom built API to solve this problem. This tool is in no way affiliated with HUD but provides a quick way to access HUD data for the years 2000 - 2021. It works as follows:</p>
    <h3 id="base-url">Base URL</h3>
    <p><a href="https://hud-mfi-api.herokuapp.com/">https://hud-mfi-api.herokuapp.com/</a></p>
    <p>The above URL is the address to access the API. Going to that address currently will bring up empty page, but this address is important because it serves as the prefix for other addresses that will return relevant data.</p>
    <h3 id="get-mfi-for-every-county-in-the-nation">Get MFI for every county in the Nation</h3>
    <p><code>getall/</code></p>
    <p><a href="https://hud-mfi-api.herokuapp.com/getall">https://hud-mfi-api.herokuapp.com/getall</a></p>
    <p>Going to this URL will return the data for every county.</p>
    <h3 id="get-mfi-for-every-county-in-a-state">Get MFI for every County in a State</h3>
    <p>The following addresses will return the county median family income estimates for every county within the user entered state. </p>
    <p><code>get/state/USER_ENTERED_STATE_ABBREVIATION</code></p>
    <p><a href="https://hud-mfi-api.herokuapp.com/get/state/OR">https://hud-mfi-api.herokuapp.com/get/state/OR</a></p>
    <h3 id="get-mfi-for-a-single-county">Get MFI for a single County</h3>
    <p>Access to data for individual counties is also possible.</p>
    <p><code>get/fips/USER_ENTERED_COUNTY_FIPS_CODE</code></p>
    <p><a href="https://hud-mfi-api.herokuapp.com/get/fips/41051">https://hud-mfi-api.herokuapp.com/get/fips/41051</a></p>
    <p>If you know the five digit county fips code, you can pass that in after the &quot;get/fips/&quot; to access the data. The above example is for Multnomah County (&quot;41051&quot;)</p>
    <p><code>get/state/USER_ENTERED_STATE_ABBREVIATION/county/USER_ENTERED_COUNTY_NAME</code></p>
    <p><a href="https://hud-mfi-api.herokuapp.com/get/state/IL/county/Cook">https://hud-mfi-api.herokuapp.com/get/state/IL/county/Cook</a></p>
    <p>To access county data by county name the user first has to pass in a state. This address is an extension of the get/state/ address. The county name has to be formatted in a specific way to work. It has to be capitalized, and including &quot; County&quot; at the end of the county name will cause the call to fail. </p>
    """
    return home_html


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
        median_income = MFI.query.filter_by(
            state_name=state_name_).filter_by(county=county_long).first()
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
