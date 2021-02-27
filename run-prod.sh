#!/bin/bash
set FLASK_APP=app/app.py
set FLASK_ENV=production
npm run build
flask digest compile
flask run
