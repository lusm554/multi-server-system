from flask import Flask, Blueprint, render_template, request as req
from flask_cors import CORS
from src.routes import users_route, chunks_route

app = Flask(__name__,
            static_url_path='',
            template_folder='static',
            static_folder='static')
app.url_map.strict_slashes = False

# add prefix '/api/v1' for routes registered in
api_bp = Blueprint('api-v1', __name__, url_prefix='/api/v1')
api_bp.register_blueprint(users_route)
api_bp.register_blueprint(chunks_route)

# add API routes
app.register_blueprint(api_bp)
CORS(app) # for testing endpoints

@app.route('/')
def get_main():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html'), 404

