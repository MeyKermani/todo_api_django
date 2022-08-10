FROM python:3.8
MAINTAINER meysamkermani@gmail.com
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /srv

COPY ./requirements.txt /srv

RUN pip install --no-cache-dir -r /srv/requirements.txt

COPY . /srv

#RUN python manage.py makemigrations
#RUN python manage.py migrate
#RUN python manage.py loaddata sample_data.json
RUN chmod +x /srv/entrypoint.sh
ENTRYPOINT ["/srv/entrypoint.sh"]
#CMD ["gunicorn", "core.wsgi", "-b 0.0.0.0:8000"]

EXPOSE 8000


