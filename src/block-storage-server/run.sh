#!/bin/sh
export FLASK_APP=./src/index.py
export export FLASK_ENV=development
flask run -h localhost -p 9090
