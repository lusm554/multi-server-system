from flask import Blueprint

bp = Blueprint('users', __name__, url_prefix='/user')

@bp.route('/')
def hello():
    return 'hello, world!'
