pybabel extract -F babel.cfg -o app/translations/messages.pot .
pybabel update -i app/translations/messages.pot -d app/translations
