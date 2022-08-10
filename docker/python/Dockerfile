FROM python:3.8
MAINTAINER meysamkermani@gmail.com
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /srv

COPY ./requirements.txt /srv

RUN pip install --no-cache-dir -r /srv/requirements.txt

COPY . /srv

RUN chmod +x /srv/entrypoint.sh
ENTRYPOINT ["/srv/entrypoint.sh"]

EXPOSE 8000


