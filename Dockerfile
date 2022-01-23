FROM python:3.9

RUN mkdir /usr/src/populatedb
WORKDIR /usr/src/populatedb

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .
