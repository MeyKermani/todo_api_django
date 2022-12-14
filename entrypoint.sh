#!/bin/sh
echo "######################   ENTRYPOINT started  ####################################"
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py makemigrations users
python manage.py makemigrations todo
python manage.py migrate

#python manage.py loaddata sample_data.json
gunicorn core.wsgi -b 0.0.0.0:8000


exec "$@"