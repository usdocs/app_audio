# Сервис преобразования wav в mp3
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=5fe620)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=5fe620)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=ffffff&color=5fe620)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=ffffff&color=5fe620)](https://www.docker.com/)
[![Gunicorn](https://img.shields.io/badge/-Gunicorn-464646?style=flat&logo=Gunicorn&logoColor=ffffff&color=5fe620)](https://gunicorn.org/)
[![nginx](https://img.shields.io/badge/-nginx-464646?style=flat&logo=nginx&logoColor=ffffff&color=5fe620)](https://nginx.org/)
[![ffmpeg](https://img.shields.io/badge/-ffmpeg-464646?style=flat&logo=ffmpeg&logoColor=ffffff&color=5fe620)](https://ffmpeg.org/)

## Описание

Данный веб-сервис, выполняет следующие функции:
- Создание пользователя;
- Для каждого пользователя - получает аудиозапись в формате wav, преобразует её в формат mp3 и записывает в базу данных, далее предоставляет ссылку для скачивания аудиозаписи.

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
- ffmpeg

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

## Автоматизация развертывания серверного ПО
Для автоматизации развертывания ПО на боевых серверах используется среда виртуализации Docker, а также Docker-compose - инструмент для запуска многоконтейнерных приложений. Docker позволяет «упаковать» приложение со всем его окружением и зависимостями в контейнер, который может быть перенесён на любую Linux -систему, а также предоставляет среду по управлению контейнерами. Таким образом, для разворачивания серверного ПО достаточно чтобы на сервере с ОС семейства Linux были установлены среда Docker и инструмент Docker-compose.

## Описание команд для запуска приложения в контейнерах
Для запуска проекта в контейнерах используем **docker-compose** : ```docker-compose up -d --build```, находясь в директории (infra) с ```docker-compose.yaml```

После сборки контейнеров выполяем:
```bash
# Выполняем миграции
docker-compose exec web python manage.py migrate
# Создаем суперппользователя
docker-compose exec web python manage.py createsuperuser
# Собираем статику со всего проекта
docker-compose exec web python manage.py collectstatic --no-input
```

**Пример POST-запросов:**

- Создание пользователя, POST:
  <br>
  URL: `http://127.0.0.1/api/v1/signup/`
  <br>
  Request body: `{"username": "user"}`
  <br>
  Response:
    `"token": "ff82a09a1fe7efd1ff7c87a2abac82406e2af0f2",
    "uuid": "19fad36a-1435-470d-8755-aafeff2c0164"`

- Добавление аудиозаписи, POST:
  <br>
  URL: `http://127.0.0.1/api/v1/audiorecord/`
  <br>
  Request body: `{"token": "ff82a09a1fe7efd1ff7c87a2abac82406e2af0f2",
    "uuid": "19fad36a-1435-470d-8755-aafeff2c0164"}`
  <br>
  Request file: аудиофайл в формате .wav
  <br>
  Response:
    `{"http://127.0.0.1/api/record/?id=720f91d9-8e25-44a3-863a-8de2dc63e8b8&user=19fad36a-1435-470d-8755-aafeff2c0164"}`

- Доступ к аудиозаписи:
  <br>
  URL: `http://127.0.0.1/api/record/?id=720f91d9-8e25-44a3-863a-8de2dc63e8b8&user=19fad36a-1435-470d-8755-aafeff2c0164`
  <br>
  Response:
    `Скачивание файла`

#### Разработчик проекта

Автор: Andrey Balakin  
E-mail: [usdocs@ya.ru](mailto:usdocs@ya.ru)