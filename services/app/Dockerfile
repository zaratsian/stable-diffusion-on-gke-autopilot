FROM nvidia/cuda:11.8.0-base-ubuntu22.04

RUN apt update && \
apt install -y software-properties-common && \
add-apt-repository ppa:deadsnakes/ppa && \
DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata &&\
apt install -y python3.9 && \
apt install -y python3-pip

WORKDIR /app

RUN python3 --version

COPY requirements.txt /app/
COPY main.py mlconfig.py /app/

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["python3", "main.py"]
