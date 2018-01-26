release: python manage.py sendalerts
web: python manage.py makemigrations & python manage.py migrate &  python manage.py ensuretriggers & gunicorn hc.wsgi --log-file -