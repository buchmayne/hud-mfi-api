import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from preprocessing_settings import db

conn = create_engine(URL(**db))
mfi_data = pd.read_sql_table(table_name='mfi', con=conn)
print(mfi_data)
