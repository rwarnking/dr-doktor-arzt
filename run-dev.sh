#!/bin/bash
export FLASK_APP=app/app.py
export FLASK_ENV=development
npm run build-dev
flask digest compile
flask run
