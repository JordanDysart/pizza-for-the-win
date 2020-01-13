#!/bin/bash

# start our db and run the flask app
export FLASK_APP=creeapi
export FLASK_ENV=development
flask init-db
flask run
