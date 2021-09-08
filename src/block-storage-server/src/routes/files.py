from flask import (
    Blueprint,
    jsonify,
    request as req
)

router = Blueprint('files', __name__, url_prefix='/chunks')

@router.route('/')
def get():
    try:
        return 'OK', 200
    except:
        return Resposne(status=500)