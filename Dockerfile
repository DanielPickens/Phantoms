
FROM python:3.8





RUN pip3 install --upgrade pip




FROM base as debug

RUN pip3 install debugpy
