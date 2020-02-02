import pandas as pd

db = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'password',
    'database': 'new_mfi_db'
}

raw_names = {
    '00': ['STATE ABREV.', 'FIPS STATE CODE', 'FIPS COUNTY CODE', 'COUNTY NAME', 'MSA NAME', 'FY 2000 MEDIAN FAMILY INCOME'],
    '01': ['STATE ABREV.', 'FIPS STATE CODE', 'FIPS COUNTY CODE', 'COUNTY NAME', 'MSA NAME', 'FY 2001 MEDIAN FAMILY INCOME'],
    '02': ['StateAlpha', 'State', 'County', 'County Name', 'MSA Name', 'Median'],
    '03': ['state_alpha', 'state', 'county', 'countyname', 'msaname', 'median2003'],
    '04': ['state_alpha', 'state', 'county', 'countyname', 'msaname', 'median2004'],
    '05': ['state_alpha', 'state', 'county', 'name', 'CountyName', 'median2005'],
    '06': ['State_Alpha', 'fips', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2006'],
    '07': ['State_Alpha', 'fips', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2007'],
    '08': ['State_Alpha', 'fips', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2008'],
    '09': ['State_Alpha', 'fips', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2009'],
    '10': ['State_Alpha', 'fips', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2010'],
    '11': ['State_Alpha', 'fips', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2011'],
    '12': ['State_Alpha', 'fips', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2012'],
    '13': ['State_Alpha', 'fips2000', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2013'],
    '14': ['State_Alpha', 'fips2000', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2014'],
    '15': ['State_Alpha', 'fips2010', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2015'],
    '16': ['State_Alpha', 'fips2010', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2016'],
    '17': ['State_Alpha', 'fips2010', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2017'],
    '18': ['State_Alpha', 'fips2010', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2018'],
    '19': ['State_Alpha', 'fips2010', 'State', 'County', 'County_Name', 'Metro_Area_Name', 'median2019']
}

territories = ['VI', 'UM', 'PR', 'MP', 'GU', 'AS']

all_counties_df = pd.read_csv('data/fips.csv', dtype=str)

folder_path = 'data/HUD_INCOME_LIMITS/'

col_order = [
    'GEOID',
    'mfi_2000',
    'mfi_2001',
    'mfi_2002',
    'mfi_2003',
    'mfi_2004',
    'mfi_2005',
    'mfi_2006',
    'mfi_2007',
    'mfi_2008',
    'mfi_2009',
    'mfi_2010',
    'mfi_2011',
    'mfi_2012',
    'mfi_2013',
    'mfi_2014',
    'mfi_2015',
    'mfi_2016',
    'mfi_2017',
    'mfi_2018',
    'mfi_2019'
]
