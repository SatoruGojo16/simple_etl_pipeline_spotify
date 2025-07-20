import dagster as dg
import pandas as pd 
from datetime import datetime   
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv('.env')

spotify_data_source_path = 'src\simple_etl_job_files\data\spotify_data.csv'
spotify_data_destination_path = 'src\simple_etl_job_files\data\spotify_data.parquet'

def extract_csv_data():
    csv_data = pd.read_csv(spotify_data_source_path,index_col=0)
    return csv_data

def transform_csv_data(csv_data):
    csv_data = csv_data[csv_data['artist_name'].notna() & csv_data['artist_name'] != '']
    csv_data['artist_name'] = csv_data['artist_name'].str.capitalize()
    remove_columns = ['reason_start', 'reason_end']
    csv_data.drop(columns=remove_columns, inplace=True, errors='ignore')
    csv_data['upload_date'] = pd.to_datetime(datetime.now(),format='%Y-%m-%d')
    return csv_data

def load_csv_to_parquet_data(csv_data):
    csv_data.to_parquet(spotify_data_destination_path,index=False)

@dg.asset(description="ETL - Load CSV data, Transform and Load as Parquet file")
def etl_csv_to_parquet_data():
    csv_data = extract_csv_data()
    csv_data = transform_csv_data(csv_data)
    load_csv_to_parquet_data(csv_data)

@dg.asset(deps=[etl_csv_to_parquet_data], description="Load transformed CSV data into PostgreSQL table")
def load_postgres_table():
    try:
        postgres_connection_string = f'postgresql://{os.getenv("POSTGRES_USERNAME")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST")}:{os.getenv("POSTGRES_PORT")}/{os.getenv("POSTGRES_DB")}'
        engine = create_engine(postgres_connection_string)
        csv_data = extract_csv_data()
        csv_data = transform_csv_data(csv_data)
        csv_data.to_sql('spotify_data', con=engine, if_exists='replace', index=False)
        return "Data loaded into PostgreSQL table successfully."
    except Exception as e:
        return f"Error loading data into PostgreSQL table: {e}"
