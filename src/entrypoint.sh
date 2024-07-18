#! /bin/bash

echo 'Waiting for postgres...'

while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done

echo 'PostgreSQL started'

echo 'Running migrations...'

python manage.py makemigrations --no-input
python manage.py migrate --no-input

python manage.py loaddata data_dump/employee.json
python manage.py loaddata data_dump/shop.json

python manage.py runserver 0.0.0.0:$DJANGO_PORT


exec "$@"