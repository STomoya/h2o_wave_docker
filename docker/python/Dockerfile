FROM python:3.11.6-alpine3.18
COPY ./docker/python/requirements.txt requirements.txt
RUN pip --default-timeout=100 install -r requirements.txt
