docker run -p 8000:8000 --env-file ./.env 63bf648aa407

python manage.py sass ./static/mainApp/sass/ ./static/mainApp/css/ --watch