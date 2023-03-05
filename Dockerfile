FROM python:3.9

# Установка переменных окружения
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Рабочая директория в Docker контейнере
WORKDIR /code

# Установка зависимостей
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копирование проекта в Docker контейнер
COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
