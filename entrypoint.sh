#!/bin/sh
poetry install --no-dev
python manage.py makemigrations
python manage.py migrate
python manage.py tailwind install
python manage.py tailwind build
python manage.py collectstatic --no-input
exec "$@"