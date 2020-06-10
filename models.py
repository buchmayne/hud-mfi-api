from app import db


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
        mfi_2020
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
            'mfi_2020': self.mfi_2020
        }
