FROM python:3.6-alpine

LABEL maintainer="antsomers@gmail.com"

WORKDIR /app/

RUN apk update && apk add mariadb-connector-c-dev alpine-sdk && rm -rf /var/cache/apk/*

COPY . /app/

RUN pip install Pipenv

RUN pipenv install --system

ENTRYPOINT ["flask", "run"]
