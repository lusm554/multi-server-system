from flask import (
    Blueprint,
    jsonify,
    request as req
)
from src.manage_dir import ManageDir
Dir = ManageDir()
router = Blueprint('files', __name__, url_prefix='/chunks')
# TODO: create opportunity to save files in user dirs

@router.route('/<chunk_url>')
def get_chunk(chunk_url):
    try:
        return 'OK', 200
    except Exception as e:
        print(e)
        return '', 500

@router.route('/<chunk_url>', methods=['POST'])
def add_chunk(chunk_url):
    try:
        print(req.files)
        if 'file' not in req.files:
            return '', 400
        file = req.files['file']
        if file.filename == '':
            return '', 400
        Dir.save(file, chunk_url)
        return 'OK', 200
    except Exception as e:
        print(e)
