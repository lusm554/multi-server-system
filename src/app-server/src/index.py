from flask import Flask, jsonify, request as req
from flask_cors import CORS
from blueprint_module import users_bp
import psycopg2
from env_config import DB_USERNAME, DB_PWD, DB_HOSTNAME, DB_PORT, DB_NAME

app = Flask(__name__)
app.register_blueprint(users_bp)
CORS(app) # for testing endpoints

@app.route('/test')
def get_main():
    return 'hello'
