release: python manage.py migrate
web: gunicorn justchat.wsgi --log-file -
web: daphne justchat.asgi:application
