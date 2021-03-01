flask backend
jinja template engine

typescript
webpack
bootstrap

# Dependencies
- Flask
    - https://flask.palletsprojects.com/en/1.1.x/installation/
    - https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
    - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
    - https://hackersandslackers.com/flask-assets/
    - https://flask.palletsprojects.com/en/1.1.x/templating/#standard-filters
- Flask-Babel
    - https://flask-babel.tkte.ch
    - https://phrase.com/blog/posts/python-localization-flask-applications/
    - https://medium.com/@nicolas_84494/flask-create-a-multilingual-web-application-with-language-specific-urls-5d994344f5fd
- Bootstrap
    - https://getbootstrap.com/docs/5.0/examples/
- Webpack
    - https://pypi.org/project/Flask-Webpack/
    - https://medium.com/@sofiaroc.pt/integrating-webpack-4-with-a-backend-framework-4a0e630d2a03
- Flags
    - https://github.com/lipis/flag-icon-css
- OpenStreetmap
    - https://wiki.openstreetmap.org/wiki/DE:OSM_mit_Leaflet/Vorbereitung
- Leaflet
    - https://leafletjs.com/examples/quick-start/

# Usefull commands
- pybabel extract -F babel.cfg -o messages.pot .
- pybabel init -i messages.pot -d app/translations -l de
- pybabel update -i messages.pot -d app/translations
