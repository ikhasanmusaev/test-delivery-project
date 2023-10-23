# Test DRF proyekt
boshlanish vaqti: 12:12 23.10 <br>
tugash vaqti: 14:40 23.10 <br>
testlar tugash vaqti: 14:58 23.10

Haqida:

- DB - postgres
- OpenAPI - swagger
- docker

Proyektni run qilish uchun

```bash
docker-compose up
```

### Agar dockerni xoslamasangiz, unda --->>

## Install

1. Создайте и активируйте виртуальное окружение (рекомендуется):

```bash
python -m venv venv
source venv/bin/activate
```

2. Установите зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

3. Настройте подключение к базе данных PostgreSQL в файле settings.py:

```
DATABASES = PSQL_CONF 
```

или

```
DATABASES = SQLITE_CONF
```

<h6> (Есть sqlite3 файл c тестовыми данными. Логин, пароль: i, string)</h6>

5. Примените миграции для создания таблиц в базе данных:

```bash
python manage.py migrate
```

6. Добавить данные:

```bash
python manage.py loaddata roles.json
```

7. Запустите сервер:

```bash
python manage.py runserver
```

Теперь вы можете перейти по адресу http://127.0.0.1:8000/docs/ в веб-браузере и
увидеть интерактивную документацию Swagger для API.
