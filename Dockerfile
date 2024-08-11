# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Указываем команду для запуска сервера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "drf_cw.wsgi:application"]