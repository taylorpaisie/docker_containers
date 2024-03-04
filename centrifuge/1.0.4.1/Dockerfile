# set global variables
ARG CENTRIFUGE_VER="1.0.2"


# build Dockerfile
FROM ubuntu:focal as builder
ARG CENTRIFUGE_VER
ARG DIAMOND_VER

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
    hmmer \
    prodigal \
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*