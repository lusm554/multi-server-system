#!/bin/sh
export FLASK_APP=./src/index.py
source $(pipenv --venv)/bin/activate
flask run -h localhost -p 8080
