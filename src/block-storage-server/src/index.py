from flask import Flask, Blueprint
from flask_cors import CORS
from src.manage_dir import ManageDir
from src.routes import files_route

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

api_bp = Blueprint('api-v1', __name__, url_prefix='/api/v1')
api_bp.register_blueprint(files_route)
app.register_blueprint(api_bp)

Dir = ManageDir()
Dir.createWorkDir()
