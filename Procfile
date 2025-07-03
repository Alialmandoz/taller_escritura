release: python manage.py collectstatic --noinput
web: gunicorn taller_escritura.wsgi --bind 0.0.0.0:$PORT