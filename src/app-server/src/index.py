from flask import Flask, jsonify, render_template, request as req
from flask_cors import CORS
from src.routes import users_route 

app = Flask(__name__,
            static_url_path='',
            template_folder='static',
            static_folder='static')
app.register_blueprint(users_route)
CORS(app) # for testing endpoints

@app.route('/')
def get_main():
    return render_template('index.html')

