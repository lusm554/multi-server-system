from functools import wraps
from flask import (
    Blueprint, 
    jsonify, 
    Response, 
    request as req
)
from src.dao.users import UsersDAO

router = Blueprint('users', __name__, url_prefix='/users')

def validate_signup_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            assert req.is_json
            data = req.get_json()
            assert 'username' in data and 'password' in data
        except Exception as e:
            msg = 'payload must be a valid json'
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper

@router.route('/', methods=['POST'])
@validate_signup_json
def signup():
    try:
        data = req.get_json()
        if UsersDAO.isUserExist(data['username']):
            return Response(status=409)
        UsersDAO.add(**data)     
        return Response(status=201)
    except Exception as e:
        print(e)
        srv_err_code = Response(status=500)
        return srv_err_code

