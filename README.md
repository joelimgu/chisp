```yaml
version: '3.8'

services:
  django:
    image: chisp:latest
    depends_on:
      - db
    environment:
      DJANGO_SECRET_KEY_FILE: /run/secrets/chisp_club_robot.secretkey
      DJANGO_DEBUG: "true"
      DJANGO_CSRF_TRUSTED_ORIGINS: https://clubrobot.joel.rs
      DJANGO_ALLOWED_HOSTS: clubrobot.joel.rs
      DJANGO_DB_NAME: chisp
      DJANGO_DB_ENGINE: django.db.backends.mysql
      DJANGO_DB_USER: root
      DJANGO_DB_PASSWORD_FILE: /run/secrets/chisp_club_robot.dbpassword
      DJANGO_DB_HOST: db
      DJANGO_DB_PORT: 3306
    secrets:
      - chisp_club_robot.secretkey
      - chisp_club_robot.dbpassword
    networks:
      backend:
      nginx:
        aliases:
          - chisp
    command: ["./wait-for-it.sh", "db:3306"]
    deploy:
      placement:
        constraints:
         - node.labels.production == true

  db:
    image: mariadb:latest
    restart: always
    volumes:
      -  chisp_club_robot_db:/var/lib/mysql
    environment:
      - MARIADB_ROOT_PASSWORD_FILE=/run/secrets/chisp_club_robot.dbpassword
      - MARIADB_DATABASE=chisp
    networks:
      backend:
        aliases:
          - db
    secrets:
      - chisp_club_robot.dbpassword
    deploy:
      placement:
        constraints:
         - node.labels.production == true

networks:
  backend:
  nginx:
    external: true
secrets:
  chisp_club_robot.secretkey:
    external: true
  chisp_club_robot.dbpassword:
    external: true
volumes:
  chisp_club_robot_db:
    external: true
```