FROM python:3.6-slim

WORKDIR /robot

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update && apt-get install make && python3.6 -m pip install -r/tmp/requirements.txt

VOLUME ["/robot"]
