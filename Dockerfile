FROM python:3 AS build

RUN apt-get update && apt-get -y install --no-install-recommends \
    libfreetype6-dev \
    libportmidi-dev \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    && rm -rf /var/lib/apt/lists/*


RUN pip3 install pygame
