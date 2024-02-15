# set global variables
ARG CHECKM2_VER="1.0.2"

# build Dockerfile
FROM ubuntu:focal as builder
ARG CHECKM2_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="CheckM2"
LABEL software.version=${CHECKM2_VER}
LABEL description="Rapid assessment of genome bin quality using machine learning."
LABEL website="https://github.com/chklovski/CheckM2"
LABEL license.url="https://github.com/chklovski/CheckM2/blob/main/LICENSE"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

ENV DEBIAN_FRONTEND=noninteractive 

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    setuptools \
    requests \
    packaging \
    tqdm \
    python3 \
    hmmer \
    scikit-learn \
    h5py \
    diamond \
    pandas \
    scipy \
    prodigal &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install checkm and its dependencies
RUN pip install --no-cache-dir \
    numpy \
    matplotlib \
    pysam

# Install CheckM2
ENV CHECKM2_DOWNLOAD git clone --recursive https://github.com/chklovski/checkm2.git && cd checkm2
ENV CHECKM2_PATH /checkm2
ENV CHECKM2_INSTALL python setup.py install

# 'CMD' instructions set a default command when the container is run.
CMD [ "checkm2", "-h" ]

# download database and inform CheckM of where the files have been placed
RUN checkm2 database --download
# ENV

# 'WORKDIR' sets working directory
WORKDIR /data

## Test ##
FROM app as test

# run test with internal test data
RUN checkm2 testrun