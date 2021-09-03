from flask import Blueprint, jsonify
from src.db import conn

bp = Blueprint('users', __name__, url_prefix='/user')

@bp.route('/')
def hello():
    cur = conn.cursor()
    cur.execute('select * from test')
    rows = cur.fetchall()
    cur.close()
    return jsonify(rows)
