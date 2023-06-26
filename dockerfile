FROM python:3.8-bullseye

ENV PYTHONBUFFERED=1

WORKDIR /mhubb

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD gunicorn memehub.wsgi:apppcation --bind 0.0.0.0:8000

EXPOSE 8000