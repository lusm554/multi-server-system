"""App configuration."""
from os import environ, path, getcwd
from dotenv import load_dotenv

# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(path.dirname(getcwd()), '.env'))

# Add env keys
DB_USERNAME = environ.get('DB_USERNAME')
DB_PWD = environ.get('DB_PWD')
DB_HOSTNAME = environ.get('DB_HOSTNAME')
DB_PORT = environ.get('DB_PORT')
DB_NAME = environ.get('DB_NAME')

