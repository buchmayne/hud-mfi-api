import pandas as pd
from sqlalchemy import create_engine, text
from configparser import ConfigParser
from sqlalchemy.engine.url import URL
from _sql import sql_queries

# define paths to HUD INCOME LIMITS data
mfi = {
    "raw_mfi_2021": "https://www.huduser.gov/portal/datasets/il/il21/Section8-FY21.xlsx",
    "raw_mfi_2020": "https://www.huduser.gov/portal/datasets/il/il20/Section8-FY20.xlsx",
    "raw_mfi_2019": "https://www.huduser.gov/portal/datasets/il/il19/Section8-FY19.xlsx",
    "raw_mfi_2018": "https://www.huduser.gov/portal/datasets/il/il18/Section8-FY18.xlsx",
    "raw_mfi_2017": "https://www.huduser.gov/portal/datasets/il/il17/Section8-FY17.xlsx",
    "raw_mfi_2016": "https://www.huduser.gov/portal/datasets/il/il16/Section8-FY16.xlsx",
    "raw_mfi_2015": "https://www.huduser.gov/portal/datasets/il/il15/Section8_Rev.xlsx",
    "raw_mfi_2014": "https://www.huduser.gov/portal/datasets/il/il14/Poverty.xls",
    "raw_mfi_2013": "https://www.huduser.gov/portal/datasets/il/il13/Section8.xls",
    "raw_mfi_2012": "https://www.huduser.gov/portal/datasets/il/il12/Section8.xls",
    "raw_mfi_2011": "https://www.huduser.gov/portal/datasets/il/il11/Section8_v3.xls",
    "raw_mfi_2010": "https://www.huduser.gov/portal/datasets/il/il10/Section8.xls",
    "raw_mfi_2009": "https://www.huduser.gov/portal/datasets/il/il09/Section8.xls",
    "raw_mfi_2008": "https://www.huduser.gov/portal/datasets/il/il08/Section8_FY08.xls",
    "raw_mfi_2007": "https://www.huduser.gov/portal/datasets/il/il07/Section8-rev.xls",
    "raw_mfi_2006": "https://www.huduser.gov/portal/datasets/il/il06/Section8FY2006.xls",
    "raw_mfi_2005": "https://www.huduser.gov/portal/datasets/il/il05/Section8FY2005.xls",
    "raw_mfi_2004": "https://www.huduser.gov/portal/datasets/IL/IL04/Section8.xls",
    "raw_mfi_2003": "https://www.huduser.gov/portal/datasets/IL/FMR03/Section8.xls",
    "raw_mfi_2002": "https://www.huduser.gov/portal/datasets/il/fmr02/prts801_02.xls",
    "raw_mfi_2001": "https://www.huduser.gov/portal/datasets/IL/FMR01/incfy01.xls",
    "raw_mfi_2000": "https://www.huduser.gov/portal/datasets/IL/FMR00/incfy00.xls",
}


def create_connection_obj():
    """Creates engine object from database.ini configuration"""
    filename = "database.ini"
    parser = ConfigParser()
    parser.read(filename)

    params = {k: v for k, v in parser.items("postgresql")}
    conn = create_engine(URL.create(**params))
    return conn


def write_raw_hud_income_limits_to_db(con, tbl_name, hud_url):
    """Read HUD income limits data with pandas and write to db

    con : sqlalchemy.Engine()
        connection engine from by sqlalchemy.create_engine
    tbl_name : str
        name to be used for database table
    hud_url : str
        link to the HUD income limits dataset
    """
    df = pd.read_excel(hud_url)
    df.columns = [
        x.lower()
        .replace("%", "pct")
        .replace("(", "_")
        .replace(")", "_")
        .replace(" ", "_")
        for x in df.columns
    ]
    df.to_sql(con=con, name=tbl_name, index=False, if_exists="replace")
    print(f"Successfully Added {tbl_name} to Database")


if __name__ == "__main__":
    conn = create_connection_obj()
    for k, v in mfi.items():
        write_raw_hud_income_limits_to_db(con=conn, tbl_name=k, hud_url=v)

    print("All HUD Income Limits data added to database")

    with conn.connect() as connection:
        for query in sql_queries:
            connection.execute(text(query))

    print("All Queries Succesfully Ran")
