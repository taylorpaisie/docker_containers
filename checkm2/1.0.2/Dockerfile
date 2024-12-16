# set global variables
ARG CHECKM2_VER="1.0.2"
ARG DIAMOND_VER="2.0.4"

# build Dockerfile
FROM ubuntu:focal AS builder
ARG CHECKM2_VER
ARG DIAMOND_VER

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

# install checkm2 and its dependencies
RUN pip install --no-cache-dir \
    numpy==1.19.5 \
    scipy==1.8.0 \
    pandas==1.4.0 \
    setuptools \
    requests \
    packaging \
    tqdm \
    scikit-learn==0.23.2 \
    h5py==2.10.0 \
    lightgbm==3.2.1 \
    protobuf==3.20.0 \
    tensorflow==2.2.0


# Clone CheckM2 repository and install
# RUN git config --global http.postBuffer 524288000 && \
#     git clone https://github.com/chklovski/checkm2.git &&\
#     cd checkm2 &&\
#     python3 setup.py install &&\
#     cd ..

RUN wget https://github.com/chklovski/CheckM2/archive/refs/tags/${CHECKM2_VER}.tar.gz && \
    tar xzf ${CHECKM2_VER}.tar.gz && \
    cd CheckM2-${CHECKM2_VER} && \
    python3 setup.py install && \
    cd ..

# Install Diamond
RUN wget http://github.com/bbuchfink/diamond/archive/v${DIAMOND_VER}.tar.gz && \
    tar xzf v${DIAMOND_VER}.tar.gz && \
    cd diamond-${DIAMOND_VER} && \
    mkdir bin && cd bin && \
    cmake .. && \
    make -j4 && \
    make install

# Running the dockerfile and tests
FROM ubuntu:focal AS app
ARG CHECKM2_VER
ARG DIAMOND_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="CheckM2"
LABEL software.version=${CHECKM2_VER}
LABEL description="Rapid assessment of genome bin quality using machine learning."
LABEL website="https://github.com/chklovski/CheckM2"
LABEL license.url="https://github.com/chklovski/CheckM2/blob/main/LICENSE"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

COPY --from=builder /usr/ /usr/

# Setting working directory
RUN mkdir data/
WORKDIR /data

# download database and set db in PATH
RUN checkm2 database --download

# # run test with internal test data
RUN checkm2 testrun

# ## Test ##
FROM app AS test

RUN apt-get update && apt-get install -y \
    python3 \
    wget

RUN mkdir ../tests/
COPY tests/ ../tests/

RUN python3 -m unittest discover -v -s ../tests

