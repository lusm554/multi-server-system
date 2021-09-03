from flask import Flask, jsonify, render_template, request as req
from flask_cors import CORS
from blueprint_module import users_bp

app = Flask(__name__,
            static_url_path='',
            template_folder='static',
            static_folder='static')
app.register_blueprint(users_bp)
CORS(app) # for testing endpoints

@app.route('/')
def get_main():
    return render_template('index.html')

