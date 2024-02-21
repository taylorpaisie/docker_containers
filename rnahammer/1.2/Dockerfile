# set global variables
ARG RNAHAMMER_VER="1.2"

# build Dockerfile
FROM ubuntu:focal as builder
ARG RNAHAMMER_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="RNAmmer"
LABEL software.version=${RNAHAMMER_VER}
LABEL description="RNAmmer predicts 5s/8s, 16s/18s, and 23s/28s ribosomal RNA in full genome sequences."
LABEL website="https://services.healthtech.dtu.dk/services/RNAmmer-1.2/"
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
    prodigal \
    hmmer \
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget https://services.healthtech.dtu.dk/download/8ec2d46a-4431-4dae-a868-e187a9ee9ae0/rnammer-1.2.Unix.tar.gz &&\
    tar xvzf rnammer-1.2.Unix.tar.gz &&\


# Running the dockerfile and tests
FROM ubuntu:focal as app
ARG RNAHAMMER_VER

COPY --from=builder /usr/ /usr/

# setting CAT to PATH
# ENV PATH="${PATH}:/CAT/CAT_pack"

# Setting working directory
RUN mkdir data/
WORKDIR /data

# ## Test ##
# FROM app as test

# RUN apt-get update && apt-get install -y \
#     python3 \
#     wget

# RUN mkdir ../tests/
# COPY tests/ ../tests/


# RUN python3 -m unittest discover -v -s ../tests


