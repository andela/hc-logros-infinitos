web: gunicorn hc.wsgi --log-file -
release: python manage.py migrate & python manage.py ensuretriggers & python manage.py sendalerts