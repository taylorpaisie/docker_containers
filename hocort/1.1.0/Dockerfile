# set global variables
ARG HOCORT_VER="1.1.0"

# build Dockerfile
FROM ubuntu:focal as builder
ARG HOCORT_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="HoCoRT"
LABEL software.version=${HOCORT_VER}
LABEL description="Remove specific organisms from sequencing reads."
LABEL website="https://github.com/ignasrum/hocort"
LABEL license.url="https://github.com/ignasrum/hocort?tab=MIT-1-ov-file#readme"
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
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install checkm2 and its dependencies
RUN pip install --no-cache-dir \
    samtools >=1.8 \
    tbb == 2020.2 \
    kraken2 >=2.1.2 \
    bowtie2 \
    hisat2 \
    bwa-mem2 \
    bbmap \
    minimap2 \
    biobloomtools



# Install HoCoRT
RUN wget https://raw.githubusercontent.com/ignasrum/hocort/main/install.sh && \ 
    wget https://raw.githubusercontent.com/ignasrum/hocort/main/environment.yml && \
    bash ./install.sh && \
    conda activate hocort


# Running the dockerfile and tests
FROM ubuntu:focal as app
ARG HOCORT_VER

COPY --from=builder /usr/ /usr/

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

