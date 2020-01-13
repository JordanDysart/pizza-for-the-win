#!/bin/bash

# install/activate virtual environment
python3 -m venv env
source env/bin/activate
pip install --upgrade pip

# Verify installation
python -V
pip -V

# install flask
pip install flask
pip install SQLAlchemy

export FLASK_APP=creeapi
export FLASK_ENV=development
export PORT=8080
