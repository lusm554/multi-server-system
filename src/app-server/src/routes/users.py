from functools import wraps
from datetime import datetime
import jwt
from src.dao.users import UsersDAO
from src.dao.sessions import SessionsDAO
from flask import (
    Blueprint,
    jsonify,
    Response,
    request as req
)

Users = UsersDAO()
Sessions = SessionsDAO()
router = Blueprint('users', __name__, url_prefix='/users')


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            assert req.is_json
            data = req.get_json()
            assert 'username' in data and 'password' in data
        except:
            msg = 'payload must be a valid json'
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper


@router.route('/', methods=['POST'])
@validate_json
def signup():
    try:
        data = req.get_json()
        if Users.isUserExist(data['username']):
            return Response(status=409)
        user = Users.add(data['username'], data['password'])
        return Response(status=204)
    except:
        return Response(status=500)


@router.route('/session', methods=['POST'])
@validate_json
def signin():
    try:
        data = req.get_json()
        if not Users.isUserExist(data['username']):
            return Response(status=409)
        EXP = 3600
        time = datetime.timestamp(datetime.now()) + EXP

        user = Users.getFullData(data['username'])
        if user['password'] != data['password']:
            return Response(status=403)

        payload = {
            'user': {
                'user_id': user['user_id'],
                'username': user['username']
            },
            'exp': time
        }
        jwtToken = jwt.encode(payload, Sessions.SECRET, algorithm='HS256')
        Sessions.add(user['user_id'], 3600, jwtToken)

        return jsonify({'auth_token': jwtToken}), 200
    except:
        return Response(status=500)


@router.route('/session', methods=['DELETE'])
def signout():
    try:
        req_token = req.headers.get('Authorization')
        if not Sessions.isTokenExist(req_token):
            return Response(status=400)
        try:
            jwt.decode(req_token, Sessions.SECRET, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'msg', 'Token expired.'}), 401

        Sessions.remove(req_token)
        return 'OK', 200
    except:
        return Response(status=500)


@router.route('/<user_name>')
def get(user_name):
    try:
        data = Users.get(user_name)
        if not data:
            return Response(status=404)
        return jsonify(data), 200
    except:
        return Response(status=500)
