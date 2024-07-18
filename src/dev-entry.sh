python manage.py makemigrations --no-input
python manage.py migrate --no-input

python manage.py loaddata data_dump/employee.json
python manage.py loaddata data_dump/shop.json

python manage.py runserver 0.0.0.0:$DJANGO_PORT

