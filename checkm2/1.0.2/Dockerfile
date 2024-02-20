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
RUN git clone https://github.com/chklovski/checkm2.git &&\
    cd checkm2 &&\
    python3 setup.py install &&\
    cd ..

# Install Diamond
RUN wget http://github.com/bbuchfink/diamond/archive/v2.0.4.tar.gz &&\
    tar xzf v2.0.4.tar.gz &&\
    cd diamond-2.0.4 &&\
    mkdir bin && cd bin &&\
    cmake -DCMAKE_INSTALL_PREFIX=$HOME .. &&\
    make -j4 &&\
    make install


# Running the dockerfile and tests
FROM ubuntu:focal as app
ARG CHECKM2_VER

COPY --from=builder /checkm2/ /checkm2/
COPY --from=builder /diamond-2.0.4/ /diamond-2.0.4/
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/

ENV PATH="${PATH}:/diamond-2.0.4/bin/"

# Setting working directory
RUN mkdir data/
WORKDIR /data

# download database and set db in PATH
RUN checkm2 database --download

# # run test with internal test data
RUN checkm2 testrun --threads 4 --debug

# ## Test ##
FROM app as test

RUN apt-get update && apt-get install -y \
    python3 \
    wget

RUN mkdir ../tests/
COPY tests/ ../tests/

RUN python3 -m unittest discover -v -s ../tests

