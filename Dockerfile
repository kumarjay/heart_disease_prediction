FROM ubuntu:18.04

#ENV PATH="/root/.local/bin:${PATH}"
#ARG PATH="/root/.local/bin:${PATH}"
EXPOSE 8000

RUN apt-get update
RUN apt-get install --assume-yes --fix-broken
RUN apt-get install -y python3 wget git
RUN apt-get install python3-pip -y
RUN apt-get install -y gcc

RUN pip3 install --upgrade pip

COPY . src/
WORKDIR /src/
RUN  pip3 install -r requirements.txt

CMD python3 main.py
