#!/bin/bash
export FLASK_APP=dr-doctor-arzt.py
export FLASK_ENV=development
export FLASK_DEBUG=1
npm run build-dev
flask digest compile
flask run
