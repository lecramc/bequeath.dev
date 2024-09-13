#!/bin/sh
poetry install
python manage.py makemigrations
python manage.py migrate
python manage.py tailwind install
python manage.py tailwind build
python manage.py collectstatic
exec "$@"