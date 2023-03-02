FROM us-docker.pkg.dev/vertex-ai/training/pytorch-gpu.1-12:latest

WORKDIR /app

COPY requirements.txt /app/
COPY main.py mlconfig.py /app/

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["python", "main.py"]
