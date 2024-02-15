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
    numpy \
    diamond \
    pandas \
    scipy \
    prodigal &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*





# ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
# ENV PATH="${PATH}:${JAVA_HOME}/bin"