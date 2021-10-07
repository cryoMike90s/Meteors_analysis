import pandas as pd
import urllib3
import certifi
import json
import sqlalchemy


def import_data_from_source():
    http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED", ca_certs=certifi.where())
    url = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
    r = http.request('GET', url)
    data = json.loads(r.data.decode('utf-8'))
    df = pd.json_normalize(data)

    return df


def processing_data():

    df = import_data_from_source()

    df.drop([':@computed_region_cbhk_fwbd', ':@computed_region_nnqa_25f4'], axis=1, inplace=True)
    df['year'] = df['year'].str[:4]
    df.dropna(inplace=True, axis=0, subset=('year', 'mass'))
    df.reset_index(inplace=True)
    df.drop('index', 1, inplace=True)
    df.index += 1
    df['year'] = df['year'].astype('int64')
    df['mass'] = df['mass'].astype('float')
    df['mass'] = df['mass'].astype('int64')
    df = df.rename(columns={'id': 'nasa_id'})
    return df


def export_to_csv():

    df = processing_data()
    df.to_csv('csv_meteor_file.csv', encoding='utf-8', index=False)

    return "Exporting data process done"


def export_to_database():

    db = sqlalchemy.create_engine('sqlite:///meteors.db')
    df = processing_data()
    df.to_sql('meteors', db, if_exists="replace")


export_to_csv()
export_to_database()
