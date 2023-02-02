FROM python:3.8
RUN apt update -y
RUN pip3 install --upgrade pip

WORKDIR /app
COPY ./src/requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt