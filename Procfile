release: rm -rf hc/api/migrations
release: python manage.py makemigrations api
release: python manage.py migrate
release: python manage.py ensuretriggers
release: python manage.py sendalerts
web: gunicorn hc.wsgi