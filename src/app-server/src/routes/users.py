from flask import Blueprint, jsonify
from src.db import conn

router = Blueprint('users', __name__, url_prefix='/user')

@router.route('/')
def hello():
    try:
        cur = conn.cursor()
        cur.execute('select * from users')
        rows = cur.fetchall()
        cur.close()
        return jsonify(rows)
    except Exception as e:
        print(e)
        return 'Error while fetching users', 500
