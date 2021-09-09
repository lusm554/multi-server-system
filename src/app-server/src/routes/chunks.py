from functools import wraps
import os
from src.dao.sessions import SessionsDAO
from src.dao.files import FilesDAO
import jwt
from flask import (
    Blueprint,
    jsonify,
    Response,
    redirect,
    request as req
)
Sessions = SessionsDAO()
Files = FilesDAO()
router = Blueprint('chunks', __name__, url_prefix='/chunks')


def validate_token(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            req_token = req.headers.get('Authorization')
            assert Sessions.isTokenExist(req_token)
        except:
            return Response(status=400)
        return f(*args, **kw)
    return wrapper

def get_from_token():
    req_token = req.headers.get('Authorization')
    try:
        return jwt.decode(req_token, Sessions.SECRET, algorithms=['HS256'])['user']
    except jwt.ExpiredSignatureError:
        return jsonify({'msg': 'Token expired.'}), 401


@router.route('/<chunk_url>')
@validate_token
def get(chunk_url):
    try:
        user = get_from_token()
        # check for valid token
        if isinstance(user, tuple):
            return user

        if not Files.isChunkExist(user['id'], chunk_url):
            return Response(status=400)

        return redirect(f'http://localhost:9090/api/v1/chunks/{chunk_url}', code=302)
    except Exception as e:
        print(e)
        return Response(status=500)


@router.route('/<chunk_url>', methods=['POST'])
@validate_token
def add(chunk_url):
    try:
        user = get_from_token()
        # check for valid token
        if isinstance(user, tuple):
            return user
        root_dir = f"root_{user['id']}"
        obj = Files.getObject(user['id'], root_dir)
        Files.createChunk(obj['object_id'], chunk_url)

        # use 307 for redirecting to POST request
        return redirect(f'http://localhost:9090/api/v1/chunks/{chunk_url}', code=307)
    except Exception as e:
        print(e)
        return Response(status=500)
