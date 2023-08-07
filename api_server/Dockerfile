FROM python:3.11.2-buster

### Setup Locale ###
ENV TZ="Asia/Seoul"
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /usr/app/api_server
COPY . /usr/app/api_server

RUN pip install --upgrade pip && pip install -r requirements.txt

### Application Run Setup ###
EXPOSE 8080
CMD uvicorn main:app --host=0.0.0.0 --port=8080 --reload