# syntax=docker/dockerfile:1
FROM python:latest
WORKDIR /usr/src/app
COPY ./chisp ./chisp
COPY ./mainApp ./mainApp
COPY ./static ./static
COPY ./requirements.txt ./requirements.txt
COPY manage.py manage.py
RUN pip install -r requirements.txt
RUN python -m pip install gunicorn
EXPOSE 8000
ENTRYPOINT python manage.py collectstatic --noinput;python manage.py migrate; gunicorn chisp.wsgi -b 0.0.0.0:8000