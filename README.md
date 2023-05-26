## Тестовое задание

## Описание

Данный проект:
- Принимает на вход POST запросы с содержимым вида {"questions_num": integer} ;
- После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов;
- Далее, полученные ответы сохраняются в базе данных, а именно следующая информация: 
     1. **ID вопроса**
     2. **Текст вопроса** 
     3. **Текст ответа**
     4. **Дата создания вопроса**

- В случае, если в БД имеется такой же вопрос, к публичному API с викторинами выполняются дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
- Ответом на запрос является предыдущий сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.


## Установка и запуск
Клонируйте репозиторий и перейдите в директорию с docker-compose
```
git clone git@github.com:usdocs/app_questions.git
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
<br>
URL: `http://127.0.0.1:8000/api/v1/questions/`
<br>
Request body: `{question_num: 100}`
<br>
Response: "Question"
