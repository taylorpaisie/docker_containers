# set global variables
ARG BAKTA_VER="1.9.2"
ARG DIAMOND_VER="2.0.14"
ARG AMRFINDER_VER="3.12.8"
ARG PILERCR_VER="1.06"

# build Dockerfile
FROM ubuntu:focal as builder
ARG BAKTA_VER
ARG DIAMOND_VER
ARG AMRFINDER_VER
ARG PILERCR_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Bakta"
LABEL software.version=${BAKTA_VER}
LABEL description="Bakta: rapid & standardized annotation of bacterial genomes, MAGs & plasmids."
LABEL website="https://github.com/oschwengers/bakta"
LABEL license.url="https://github.com/oschwengers/bakta?tab=GPL-3.0-1-ov-file#readme"
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
    gcc \
    curl \
    libcurl4-openssl-dev \
    ca-certificates \
    git \
    python3 \
    python3-pip \
    infernal \
    ncbi-blast+ \
    aragorn \
    trnascan-se \
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install checkm2 and its dependencies
RUN pip install --no-cache-dir \
    setuptools \
    requests \
    packaging \
    xopen \
    biopython \
    pyyaml \
    pyhmmer==0.10.0 \
    pyrodigal==2.1.0 \
    alive-progress \
    circos \
    bakta==1.9.2

# Install Diamond
RUN wget http://github.com/bbuchfink/diamond/archive/v${DIAMOND_VER}.tar.gz && \
    tar xzf v${DIAMOND_VER}.tar.gz && \
    cd diamond-${DIAMOND_VER} && \
    mkdir bin && cd bin && \
    cmake .. && \
    make -j4 && \
    make install

# Install NCBI-AMRFinderPlus
RUN git clone https://github.com/ncbi/amr.git && \
    cd amr && \
    git checkout master && \
    make && \
    make clean && \
    make DEFAULT_DB_DIR=/usr/amrfinder/data && \
    make install INSTALL_DIR=$HOME/amrfinder

# Install piler-cr
RUN mkdir pilercr && cd pilercr && \
    wget https://www.drive5.com/pilercr/pilercr${PILERCR_VER}.tar.gz && \
    tar xvzf pilercr${PILERCR_VER}.tar.gz

# Running the dockerfile and tests
FROM ubuntu:focal as app
ARG CHECKM2_VER
ARG DIAMOND_VER
ARG AMRFINDER_VER
ARG PILERCR_VER

COPY --from=builder /usr/ /usr/
COPY --from=builder /amr/ /amr/
COPY --from=builder /pilercr/ /pilercr/

ENV PATH="${PATH}:/amr/"
ENV PATH="${PATH}:/pilercr/"

# Setting working directory
# RUN mkdir data/
# WORKDIR /data

# RUN bakta --help && \
#     bakta_db --help && \
#     bakta --version

# RUN bakta_db list && \
#     bakta_db download --type light 
