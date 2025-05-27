FROM python:3.11-slim AS base

ENV PYTHONUNBUFFERED=1

WORKDIR /punk_recognizer

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
