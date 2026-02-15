FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD gunicorn jdante.wsgi:application --bind 0.0.0.0:$PORT
