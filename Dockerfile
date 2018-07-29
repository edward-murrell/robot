FROM python:3.6-slim

RUN apt-get update && apt-get install make

WORKDIR /robot

COPY ./ /robot
