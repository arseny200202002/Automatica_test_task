# Automatica_test_task
## Инструкция по запуску 
### Запуск в докере
1. Необходимо оказаться в корневой директории 
2. Далее запускаем команду: `docker-compose up --build`
3. Дожидаемся сообщения от сервера джанго о начале работы на порту `8080`

### Запуск локально
1. Создаем venv командой: 
    - python -m venv venv
2. Активируем venv командой: 
    - venv/scripts/activate
3. Устанавливаем все необходимые зависимости командой: 
    - pip install -r > requirements.txt
4. Запускаем PGadmin и создаем базу данных с любым названием для выбранного пользователя
5. Заполняем конфигурационный файл `.env` следующими данными:
    - DB_NAME - название созданной БД
    - DB_USER - имя пользователя БД
    - DB_PASSWORD - пароль от пользователя БД
    - DJANGO_PORT - порт для заупска сервера с приложением
6. Применяем миграции к БД командами: 
    - python manage.py makemigrations
    - python manage.py migrate
7. Загружаем в БД тестовые данные командами:
    - python manage.py loaddata data_dump/employee.json
    - python manage.py loaddata data_dump/shop.json
8.  Создаем суперпользователя для использования админ панели:
    - python manage.py createsuperuser    
9. Запускаем сервер командой:
    - python manage.py runserver localhost:8000

ЛИБО можно осуществить запуск при помощи скрипта: `dev-entry.sh`