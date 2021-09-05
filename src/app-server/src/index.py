from flask import Flask, Blueprint, render_template, request as req
from flask_cors import CORS
from src.routes import users_route 

app = Flask(__name__,
            static_url_path='',
            template_folder='static',
            static_folder='static')

# add prefix '/api/v1' for routes registered in
api_bp = Blueprint('api-v1', __name__, url_prefix='/api/v1')
api_bp.register_blueprint(users_route)

# add API routes
app.register_blueprint(api_bp)
CORS(app) # for testing endpoints

@app.route('/')
def get_main():
    return render_template('index.html')

