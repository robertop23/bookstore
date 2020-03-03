# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# fix for Pillow
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/backend/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/backend/

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/backend/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]
