# syntax=docker/dockerfile:1
FROM python:latest
RUN pip install pipenv
WORKDIR /usr/src/app
COPY ./chisp ./chisp
COPY ./mainApp ./mainApp
COPY ./static ./static
COPY manage.py Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
RUN ["/bin/bash", "-c", "BUILDING=TRUE python manage.py sass static/mainApp/sass static/mainApp/css"]
RUN ["/bin/bash", "-c", "BUILDING=TRUE python manage.py collectstatic --noinput"]
EXPOSE 8000
ENTRYPOINT python manage.py migrate; gunicorn chisp.wsgi -b 0.0.0.0:8000