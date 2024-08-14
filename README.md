# Запуск проекта

Чтобы запустить проект, выполните следующие шаги:

1. Установите Docker и Docker Compose на вашем сервере.
2. Клонируйте репозиторий проекта на ваш сервер.
3. Перейдите в папку проекта и выполните команду `docker-compose up -d`.
4. Проект будет доступен по адресу `http://ваш_сервер:8000`.

# Настройка окружения

Чтобы настроить окружение, вам нужно будет создать файл `.env` в папке проекта. В этом файле вы должны указать следующие переменные:

* `DB_NAME`: имя базы данных
* `DB_USER`: имя пользователя БД
* `DB_PASSWORD`: пароль БД
* `DB_HOST`: адрес сервера БД
* `DB_PORT`: порт  БД

* `CELERY_APP`: имя приложения celery
* `REDIS_HOST`: адрес Redis сервера
* `CELERY_BROKER_URL`: URL брокера Celery
* `CELERY_RESULT_BACKEND`: URL бэкенда Celery

Пример файла `.env`:
```makefile
REDIS_HOST=localhost
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0