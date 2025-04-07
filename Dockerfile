FROM ubuntu:22.04

MAINTAINER Utkarsh Singh

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3  pip mysql-server libmysqlclient-dev python3-dev build-essential \
    vim mc wget curl && apt-get clean

RUN pip3 install --upgrade pip

RUN pip install mysql-connector-python

EXPOSE 3306

ENV FOLDER_PROJECT=/var/python_mysql_docker_1_0

RUN mkdir -p $FOLDER_PROJECT


COPY docker_run_mysql.sh $FOLDER_PROJECT
COPY start.sql $FOLDER_PROJECT
COPY src $FOLDER_PROJECT
RUN chmod +x ${FOLDER_PROJECT}/docker_run_mysql.sh
CMD ["/var/python_mysql_docker_1_0/docker_run_mysql.sh"]