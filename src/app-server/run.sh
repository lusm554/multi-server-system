#!/bin/sh
export FLASK_APP=./src/index.py
flask run -h localhost -p 8080
