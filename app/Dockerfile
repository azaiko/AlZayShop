# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем требования проекта
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y postgresql-client

# Копируем весь проект в контейнер
COPY . /app/

# Открываем порт, на котором будет работать Django
EXPOSE 8000

# Устанавливаем команду для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
COPY wait-for-db.sh /wait-for-db.sh
RUN chmod +x /wait-for-db.sh