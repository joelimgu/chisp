docker run -p 8000:8000 --env-file ./.env 63bf648aa407

python manage.py sass ./static/mainApp/sass/ ./static/mainApp/css/ --watch




version: '3'
services:
django:
image: clubrobotinsa/chisp:0.0.2
depends_on:
- db
volumes:
- static-files:/www/static/
environment:
- DJANGO_SECRET_KEY=(rwej%nhfqyo_8et98gfklb9!q2e4hdz%ah%@bcq2i^coqoqm9
- DJANGO_DEBUG=False
- URL=clubrobot.joelimgu.me
# Database options
- DB_NAME=django
- DB_USER=root
- DB_PASSWORD=example
- DB_HOST=db
- DB_PORT=3306
networks:
- backend
command: ["./wait-for-it.sh", "db:3306"]

nginx:
image: nginx:stable
restart: always
ports:
- 7001:80
environment:
- DJANGO_HOST=django
- URL=http://django:8000
volumes:
- ./nginx-templates:/etc/nginx/templates/
- static-files:/www/static
networks:
- backend

db:
image: mariadb:latest
restart: always
volumes:
-  db:/var/lib/mysql
environment:
- MARIADB_ROOT_PASSWORD=example
- MARIADB_DATABASE=django
networks:
- backend

networks:
backend:

volumes:
static-files:
db: