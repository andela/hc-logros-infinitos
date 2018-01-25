release: python manage.py ensuretriggers & python manage.py sendalerts
web: python manage.py migrate &  gunicorn hc.wsgi --log-file -