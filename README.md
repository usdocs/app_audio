## Тестовое задание

## Описание

Данный веб-сервис, выполняет следующие функции:
- Создание пользователя;
- Для каждого пользователя - сохраняет аудиозапись в формате wav, преобразует её в формат mp3 и записывает в базу данных, далее предоставляет ссылку для скачивания аудиозаписи.



## Установка и запуск
Клонируйте репозиторий и перейдите в директорию с docker-compose
```
git clone git@github.com:usdocs/app_audio.git
cd infra
```

Запустите docker-compose:
```
docker-compose up -d --build
```

После сборки контейнеров выполяем:
```bash
# Выполняем миграции
docker-compose exec web python manage.py migrate
# Создаем суперпользователя
docker-compose exec web python manage.py createsuperuser
# Собираем статику со всего проекта
docker-compose exec web python manage.py collectstatic --no-input
```

## Стек технологий:
- Python 3
- Django 3.2
- Django ORM
- DRF (Django REST framework)
- Gunicorn
- nginx
- Docker
- Docker-compose
- PostgreSQL
- GIT

## Шаблон наполнения .env
```
# указываем, с какой БД работаем
DB_ENGINE=django.db.backends.postgresql
# имя базы данных
DB_NAME=
# логин для подключения к базе данных
POSTGRES_USER=
# пароль для подключения к БД
POSTGRES_PASSWORD=
# название сервиса (контейнера)
DB_HOST=
# порт для подключения к БД
DB_PORT=
# секретный ключ Django
SECRET_KEY=
```

**Пример POST-запроса:**

- Создание пользователя, POST:
  <br>
  URL: `http://127.0.0.1:8000/api/v1/signup/`
  <br>
  Request body: `{username: user}`
  <br>
  Response:
    `"token": "ff82a09a1fe7efd1ff7c87a2abac82406e2af0f2",
    "uuid": "19fad36a-1435-470d-8755-aafeff2c0164"`

- Добавление аудиозаписи, POST:
  <br>
  URL: `http://127.0.0.1:8000/api/v1/audiorecord/`
  <br>
  Request body: `{"token": "ff82a09a1fe7efd1ff7c87a2abac82406e2af0f2",
    "uuid": "19fad36a-1435-470d-8755-aafeff2c0164"}`
  <br>
  Request file: аудиофайл в формате .wav
  <br>
  Response:
    `"token": "ff82a09a1fe7efd1ff7c87a2abac82406e2af0f2",
    "uuid": "19fad36a-1435-470d-8755-aafeff2c0164"`

- Доступ к аудиозаписи:
  <br>
  URL: `http://127.0.0.1:8000/api/v1/audiorecord/`
  <br>
  Request body: `{username: user}`
  <br>
  Response:
    `"token": "ff82a09a1fe7efd1ff7c87a2abac82406e2af0f2",
    "uuid": "19fad36a-1435-470d-8755-aafeff2c0164"`
