FROM python:3.9.17-alpine3.18

RUN apk update && apk add --no-cache xorg-server xvfb

RUN addgroup app && adduser -S -G app app
RUN apk add --no-cache tk

USER app
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENV DISPLAY=:0
CMD python main.py