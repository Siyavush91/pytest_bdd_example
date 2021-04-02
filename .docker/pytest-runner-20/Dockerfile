FROM python:3.9-slim-buster
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt-dev \
    libssl-dev \
    zlib1g-dev \
    gcc \
    && apt-get clean autoclean \
    && apt-get autoremove --yes \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /tmp/reqs.txt
RUN pip3 install -r /tmp/reqs.txt