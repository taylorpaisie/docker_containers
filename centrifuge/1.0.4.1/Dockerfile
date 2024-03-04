# set global variables
ARG CENTRIFUGE_VER="1.0.2"

# build Dockerfile
FROM ubuntu:focal as builder
ARG CENTRIFUGE_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Centrifuge"
LABEL software.version=${CENTRIFUGE_VER}
LABEL description="Classifier for metagenomic sequences."
LABEL website="https://github.com/DaehwanKimLab/centrifuge"
LABEL license.url="https://github.com/DaehwanKimLab/centrifuge?tab=GPL-3.0-1-ov-file#readme"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

ENV DEBIAN_FRONTEND=noninteractive 

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    unzip \
    less \
    automake \
    cmake \
    zlib1g-dev\
    libzstd-dev \
    g++ \
    python3 \
    python3-pip \
    git \
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/DaehwanKimLab/centrifuge && \
    cd centrifuge &&\
    make && \
    make install prefix=/usr/local

# Running the dockerfile and tests
FROM ubuntu:focal as app
ARG CENTRIFUGE_VER

COPY --from=builder /usr/ /usr/
# COPY --from=builder /usr/local/ /usr/local/

ENV PATH="${PATH}:/usr/"

# Setting working directory
RUN mkdir data/
WORKDIR /data

