flask backend
jinja template engine

typescript
webpack
bootstrap

# Dependencies
- Flask
    - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
- Flask-Babel
    - https://flask-babel.tkte.ch
    - https://phrase.com/blog/posts/python-localization-flask-applications/
    - https://medium.com/@nicolas_84494/flask-create-a-multilingual-web-application-with-language-specific-urls-5d994344f5fd
- Bootstrap

# Usefull commands
- pybabel extract -F babel.cfg -o messages.pot .
- pybabel init -i messages.pot -d translations -l de
- pybabel update -i messages.pot -d translations
