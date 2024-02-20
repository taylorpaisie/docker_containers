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
    # libpthread \
    # zlib \
    cmake \
    gcc \
    python3 \
    python3-pip \
    git \
    hmmer \
    prodigal \
    ncbi-blast+ \
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install checkm2 and its dependencies
RUN pip install --no-cache-dir \
    numpy \
    pysam \
    scipy \
    pandas \
    # diamond \
    # diamond-aligner \
    setuptools \
    requests \
    packaging \
    tqdm \
    scikit-learn==0.23.2 \
    h5py \
    lightgbm \
    tensorflow 

# Install Diamond
# RUN wget http://github.com/bbuchfink/diamond/releases/download/v2.1.9/diamond-linux64.tar.gz
# RUN tar xzf diamond-linux64.tar.gz

# RUN wget http://github.com/bbuchfink/diamond/archive/v2.1.9.tar.gz &&\
#     tar xzf v2.1.9.tar.gz &&\
#     cd diamond-2.1.9 &&\
#     mkdir bin &&\
#     cd bin &&\
#     cmake .. &&\
#     make -j4 &&\
#     sudo make install

# Clone CheckM2 repository and install
RUN git clone https://github.com/chklovski/checkm2.git &&\
    cd checkm2 &&\
    python3 setup.py install

# Running the dockerfile and tests
FROM ubuntu:focal as app
ARG CHECKM2_VER

COPY --from=builder /checkm2/ /checkm2
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/

ENV PATH="${PATH}:/${CHECKM2_PATH}/bin"

# Setting working directory
RUN mkdir data/
WORKDIR /data

# download database and set db in PATH
RUN checkm2 database --download
# RUN wget -nv https://zenodo.org/records/5571251/files/checkm2_database.tar.gz?download=1 -O checkm2_database.tar.gz
ENV PATH="${PATH}:/root/databases/CheckM2_database/"

# run test with internal test data
# RUN checkm2 testrun --threads 4 \
#     --database_path /root/databases/CheckM2_database/uniref100.KO.1.dmnd

## Test ##
FROM app as test

RUN apt-get update && apt-get install -y \
    python3 \
    wget

RUN mkdir ../tests/
COPY tests/ ../tests/

RUN python3 -m unittest discover -v -s ../tests

