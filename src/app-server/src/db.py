import psycopg2
from src.env_config import DB_USERNAME, DB_PWD, DB_HOSTNAME, DB_PORT, DB_NAME
from src.managedb import ManageDB

conn_url = f'postgresql://{DB_USERNAME}:{DB_PWD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}'

try:
    conn = psycopg2.connect(conn_url)
except Exception as main_conn_err:
    if not str(main_conn_err).startswith(f'FATAL:  database "{DB_NAME}" does not exist'):
        raise main_conn_err
    try:
        print(f'Database {DB_NAME} does not exist, creating...')
        conn = psycopg2.connect(conn_url[0:len(conn_url) - len(DB_NAME)])
        ManageDB(conn).setupDatabase()
    except Exception as sub_conn_err:
        raise sub_conn_err

