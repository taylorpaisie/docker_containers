# set global variables
ARG CAT_VER="5.3"
ARG DIAMOND_VER="2.1.9"

# build Dockerfile
FROM ubuntu:focal as builder
ARG CAT_VER
ARG DIAMOND_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="CAT"
LABEL software.version=${CAT_VER}
LABEL description="CAT: a tool for taxonomic classification of contigs and metagenome-assembled genomes (MAGs)."
LABEL website="https://github.com/dutilh/CAT"
LABEL license.url="https://github.com/dutilh/CAT/blob/master/LICENSE.md"
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
    python3 \
    python3-pip \
    git \
    prodigal \
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install CAT dependencies
RUN pip install --no-cache-dir \
    certifi \
    biopython

# clone CAT from git repo    
RUN wget https://github.com/dutilh/CAT/archive/refs/tags/v${CAT_VER}.tar.gz &&\
    tar xvzf v${CAT_VER}.tar.gz &&\
    cd CAT-${CAT_VER}/ &&\
    chmod +x CAT_pack/CAT &&\
    cd ..

# Set CAT/BAT in path
ENV PATH="${PATH}:/CAT/CAT_pack"

# Install Diamond
RUN wget http://github.com/bbuchfink/diamond/archive/v${DIAMOND_VER}.tar.gz &&\
    tar xzf v${DIAMOND_VER}.tar.gz &&\
    cd diamond-${DIAMOND_VER} &&\
    mkdir bin && cd bin &&\
    cmake .. &&\
    make -j4 &&\
    make install

# Running the dockerfile and tests
FROM ubuntu:focal as app
ARG CAT_VER
ARG DIAMOND_VER

COPY --from=builder /usr/ /usr/
COPY --from=builder /CAT-${CAT_VER}/ /CAT/

# setting CAT to PATH
ENV PATH="${PATH}:/CAT/CAT_pack"

# Setting working directory
RUN mkdir data/ &&\
    cd data/ &&\
    mkdir db_tests/
WORKDIR /data

RUN gzip -d ../CAT/tests/data/prepare/small.fa.gz
RUN CAT prepare --db_fasta \
    ../CAT/tests/data/prepare/small.fa \
    --acc2tax ../CAT/tests/data/prepare/prot2acc.txt \
    --names ../CAT/tests/data/prepare/names.dmp \
    --nodes ../CAT/tests/data/prepare/nodes.dmp \
    --db_dir db_tests/

RUN CAT contigs -c ../CAT/tests/data/contigs/small_contigs.fa \
    -d db_tests/db/ -t db_tests/tax/

# ## Test ##
# FROM app as test

# RUN apt-get update && apt-get install -y \
#     python3 \
#     wget

# RUN mkdir ../tests/
# COPY tests/ ../tests/


# RUN python3 -m unittest discover -v -s ../tests