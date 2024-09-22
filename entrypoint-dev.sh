#!/bin/sh
poetry install --only main
python manage.py makemigrations
python manage.py migrate
python manage.py tailwind install
python manage.py collectstatic --no-input
python manage.py runscript load_fixtures
python manage.py runserver 0.0.0.0:8000
exec "$@"