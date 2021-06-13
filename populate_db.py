import os
import re
from functools import reduce
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from preprocessing_settings import db, raw_names, territories, all_counties_df, folder_path, col_order


def add_zeros_county(str):
    if len(str) == 3:
        return str
    elif len(str) == 2:
        return '0{}'.format(str)
    elif len(str) == 1:
        return '00{}'.format(str)
    else:
        return None


def add_zeros_state(str):
    if len(str) == 2:
        return str
    elif len(str) == 1:
        return '0{}'.format(str)
    else:
        return None


def load_ami_data(file_path):
    '''
    Input:
        file_path: str
            Path to file downloaded from HUD containing county income limits
    Output:
        out_df: pd.DataFrame
            Dataframe containing both fips_code and median income for that year
    '''
    data_year = re.search(r"\d{2}(?=\.xlsx*)", file_path).group(0)
    mfi_col = 'mfi_20{}'.format(data_year)

    raw_data = pd.read_excel(file_path, dtype=str)
    df = raw_data[raw_names[data_year]].copy()

    if int(data_year) < 6:
        df.columns = ['State_Alpha', 'State', 'County', 'County_Name', 'Metro_Area_Name', mfi_col]
    else:
        df.columns = ['State_Alpha', 'GEOID', 'State', 'County', 'County_Name', 'Metro_Area_Name', mfi_col]

    df['State'] = df['State'].apply(add_zeros_state)
    df['County'] = df['County'].apply(add_zeros_county)
    df['GEOID'] = df['State'] + df['County']

    df = df[(~df['State_Alpha'].isin(territories)) & (df['GEOID'].isin(county_fips))]
    df[mfi_col] = df[mfi_col].astype(int)

    out_df = df[['GEOID', mfi_col]].drop_duplicates().groupby('GEOID').min().reset_index()
    out_df.sort_values('GEOID', inplace=True)

    return out_df


if __name__ == "__main__":
    county_fips = all_counties_df['GEOID'].tolist()
    # conn = create_engine(URL(**db))
    conn = create_engine(os.environ.get("DATABASE_URL"))

    file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path)]
    list_mfi_dfs = [load_ami_data(file_path) for file_path in file_paths]

    mfi_df = reduce(lambda left, right: pd.merge(left, right, on='GEOID', how='inner'), list_mfi_dfs)
    mfi_df = mfi_df[col_order]
    mfi_df = pd.merge(mfi_df, all_counties_df, how='inner')
    mfi_df.rename(columns={'GEOID': 'geoid'}, inplace=True)

    mfi_df.to_sql(
        name='mfi',
        con=conn,
        if_exists='replace',
        index=False,
        index_label='geoid'
        )
