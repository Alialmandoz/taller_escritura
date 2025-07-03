release: python manage.py collectstatic --noinput && python manage.py migrate
web: gunicorn taller_escritura.wsgi