# set global variables
ARG CENTRIFUGE_VER="1.0.4.1"
ARG BLASTPLUS_VER="2.15.0"

# build Dockerfile
FROM ubuntu:focal as builder
ARG CENTRIFUGE_VER
ARG BLASTPLUS_VER

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
    zlib1g-dev \
    libzstd-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libjson-perl \
    libgdbm-dev \
    libssl-dev \
    libbz2-dev \
    libc6-dev \
    g++ \
    python \
    git \
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

RUN wget --no-check-certificate https://github.com/DaehwanKimLab/centrifuge/archive/refs/tags/v1.0.4.1.tar.gz && \
    tar xvf v${CENTRIFUGE_VER}.tar.gz && \
    cd centrifuge-${CENTRIFUGE_VER} && \
    make && \
    make install prefix=/usr/local

# Install BLAST+
RUN wget --no-check-certificate https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.15.0/ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz && \
    tar xvf ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz && \
    mv ncbi-blast-${BLASTPLUS_VER}+/bin/* /usr/local/bin

ENV PATH="${PATH}:/centrifuge-${CENTRIFUGE_VER}"
ENV PATH="${PATH}:/usr/local/bin"

# # Running the dockerfile and tests
FROM ubuntu:focal as app
ARG CENTRIFUGE_VER
ARG BLASTPLUS_VER

COPY --from=builder /centrifuge-${CENTRIFUGE_VER}/ /centrifuge-${CENTRIFUGE_VER}/
COPY --from=builder /usr/ /usr/

# # Setting working directory
RUN mkdir data/
WORKDIR /data

RUN centrifuge-build --conversion-table \
    ../centrifuge-1.0.4.1/example/reference/gi_to_tid.dmp \
    --taxonomy-tree ../centrifuge-1.0.4.1/example/reference/nodes.dmp \
    --name-table ../centrifuge-1.0.4.1/example/reference/names.dmp \
    ../centrifuge-1.0.4.1/example/reference/test.fa test

RUN centrifuge -f -x test ../centrifuge-1.0.4.1/example/reads/input.fa


# ## Test ##
# FROM app as test

# RUN apt-get update && apt-get install -y \
#     python3 \
#     wget

# RUN mkdir ../tests/
# COPY tests/ ../tests/


# RUN python3 -m unittest discover -v -s ../tests

