import pandas as pd
from sqlalchemy import create_engine
from configparser import ConfigParser
from sqlalchemy.engine.url import URL

# load database connection parameters and create engine
filename = 'database.ini'

parser = ConfigParser()
parser.read(filename)

params = {}
for k, v in parser.items('postgresql'):
    params[k] = v


conn = create_engine(URL(**params))

# define paths to HUD INCOME LIMITS data
mfi = {
    'raw_mfi_2021': "https://www.huduser.gov/portal/datasets/il/il21/Section8-FY21.xlsx",
    'raw_mfi_2020': "https://www.huduser.gov/portal/datasets/il/il20/Section8-FY20.xlsx",
    'raw_mfi_2019': "https://www.huduser.gov/portal/datasets/il/il19/Section8-FY19.xlsx",
    'raw_mfi_2018': "https://www.huduser.gov/portal/datasets/il/il18/Section8-FY18.xlsx",
    'raw_mfi_2017': "https://www.huduser.gov/portal/datasets/il/il17/Section8-FY17.xlsx",
    'raw_mfi_2016': "https://www.huduser.gov/portal/datasets/il/il16/Section8-FY16.xlsx",
    'raw_mfi_2015': "https://www.huduser.gov/portal/datasets/il/il15/Section8_Rev.xlsx",
    'raw_mfi_2014': "https://www.huduser.gov/portal/datasets/il/il14/Poverty.xls",
    'raw_mfi_2013': "https://www.huduser.gov/portal/datasets/il/il13/Section8.xls"
}


# write raw mfi
def write_raw_hud_income_limits_to_db(tbl_name, hud_url):
    '''Read HUD income limits data with pandas and write to db

    tbl_name : str
        name to be used for database table
    hud_url : str
        link to the HUD income limits dataset
    '''
    df = pd.read_excel(hud_url)
    df.columns = [x.lower() for x in df.columns]
    df.to_sql(con=conn, name=tbl_name, index=False, if_exists='replace')
    print(f"Successfully Added {tbl_name} to Database")


if __name__ == '__main__':
    for k, v in mfi.items():
        write_raw_hud_income_limits_to_db(tbl_name=k, hud_url=v)

    print("All HUD income limits data added to database")
