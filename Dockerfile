FROM python:3.8

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install requirements.txt

COPY . .
