release: python manage.py migrate
web: daphne -b 0.0.0.0 -p 8001 justchat.asgi:application
web: gunicorn justchat.wsgi --log-file -
