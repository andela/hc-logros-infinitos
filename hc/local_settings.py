import os

SITE_ROOT = "https://hc-logros.herokuapp.com"
SITE_NAME = "Health Checks"
DEFAULT_FROM_EMAIL = "healthchecks@example.org"

# Email
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True