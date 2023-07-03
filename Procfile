release: python manage.py migrate
web: waitress-serve --port=8000 --host=127.0.0.1 storefront.wsgi:application
worker: celery -A storefront worker