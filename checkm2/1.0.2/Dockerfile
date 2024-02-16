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
    python3 \
    python3-pip \
    git \
    hmmer \
    diamond-aligner \
    prodigal \
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install checkm and its dependencies
RUN pip install --no-cache-dir \
    numpy \
    matplotlib \
    pysam \
    scipy \
    pandas \
    setuptools \
    requests \
    packaging \
    tqdm \
    scikit-learn \
    h5py \
    lightgbm \
    tensorflow

# Clone CheckM2 repository and install
RUN git clone https://github.com/chklovski/checkm2.git &&\
    cd checkm2 &&\
    python3 setup.py install


# # Running the dockerfile and tests
FROM ubuntu:focal as app
ARG CHECKM2_VER

COPY --from=builder /checkm2/ /checkm2
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/

ENV PATH="${PATH}:/${CHECKM2_PATH}/bin"

# # 'WORKDIR' sets working directory
RUN mkdir data/
WORKDIR /data

# download database and inform CheckM of where the files have been placed
# RUN mkdir /data/db/ && \
#     cd /data/db/ && \
#     for i in 1 2 3; do \
#         checkm2 database --download && break || sleep 15; \
#     done

RUN checkm2 database --download

ENV PATH="${PATH}:/root/databases/"

# # run test with internal test data
# RUN checkm2 testrun

# ## Test ##
FROM app as test

RUN apt-get update && apt-get install -y \
    python3 \
    wget

RUN mkdir ../tests/
COPY tests/ ../tests/

RUN python3 -m unittest discover -v -s ../tests

