FROM python:3.11-slim

WORKDIR /app
COPY . .


RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt


CMD ["python", "main.py"]
