release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py ensuretriggers
release: python manage.py sendalerts
web: gunicorn hc.wsgi --log-file -
