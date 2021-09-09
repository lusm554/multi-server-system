from flask import (
    Blueprint,
    jsonify,
    Response,
    send_file,
    request as req
)
from src.manage_dir import ManageDir
Dir = ManageDir()
router = Blueprint('files', __name__, url_prefix='/chunks')
# TODO: create opportunity to save files in user dirs

@router.route('/<chunk_url>')
def get_chunk(chunk_url):
    try:
        file = Dir.find(chunk_url)
        if not file:
            return Response(status=400)
        return send_file(file, as_attachment=True)
    except:
        return Response(status=500)

@router.route('/<chunk_url>', methods=['POST'])
def add_chunk(chunk_url):
    try:
        print(req.files)
        if 'file' not in req.files:
            return Response(status=400)
        file = req.files['file']
        if file.filename == '':
            return Response(status=400)
        Dir.save(file, chunk_url)
        return Response(status=200)
    except:
        return Response(status=500)
