release: python manage.py ensuretriggers
release: python manage.py sendalerts
web: python manage.py makemigrations & python manage.py migrate & gunicorn hc.wsgi --log-file -
