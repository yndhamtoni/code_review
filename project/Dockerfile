FROM python:3.10.12
RUN apt-get update
RUN pip install --upgrade pip
RUN mkdir /project
COPY . /project
COPY requirements.txt /project
WORKDIR /project
RUN pip install -r requirements.txt
