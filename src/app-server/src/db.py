import psycopg2
from src.env_config import DB_USERNAME, DB_PWD, DB_HOSTNAME, DB_PORT, DB_NAME

conn_url = f'postgresql://{DB_USERNAME}:{DB_PWD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}'
conn = psycopg2.connect(conn_url)
