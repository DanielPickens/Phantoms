FROM python:3.8-alpine as base

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev libffi-dev jpeg-dev zlib-dev geos sdl2\ 
    && rm -rf /var/cache/apk/*

RUN pip3 install --upgrade pip
RUN pip3 install pygame