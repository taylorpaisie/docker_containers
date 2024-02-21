# set global variables
ARG CAT_VER="5.3"

# build Dockerfile
FROM ubuntu:focal as builder
ARG CAT_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="CAT"
LABEL software.version=${CAT_VER}
LABEL description="CAT: a tool for taxonomic classification of contigs and metagenome-assembled genomes (MAGs)."
LABEL website="hhttps://github.com/dutilh/CAT"
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
    g++ \
    python3 \
    python3-pip \
    git \
    # hmmer \
    prodigal \
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# clone CAT from git repo
RUN git clone https://github.com/dutilh/CAT.git &&\
    cd CAT/ &&\
    chmod +x CAT_pack/CAT &&\
    cd ..

# Add CAT and BAT to PATH
ENV PATH="/CAT/CAT_pack:${PATH}"

# Install Diamond
RUN wget http://github.com/bbuchfink/diamond/archive/v2.1.9.tar.gz &&\
    tar xzf v2.1.9.tar.gz &&\
    cd diamond-2.1.9 &&\
    mkdir bin && cd bin &&\
    cmake .. &&\
    make -j4 &&\
    make install

# Running the dockerfile and tests
FROM ubuntu:focal as app
ARG CAT_VER

COPY --from=builder /usr/ /usr/

# Setting working directory
RUN mkdir data/
WORKDIR /data

# setting CAT to PATH
ENV PATH="${PATH}:/CAT/CAT_pack"

# download database
# RUN wget --no-check-certificate tbb.bio.uu.nl/tina/CAT_prepare/20231120_CAT_nr.tar.gz &&\
#     tar -xvzf 20231120_CAT_nr.tar.gz


# ## Test ##
# FROM app as test

# RUN apt-get update && apt-get install -y \
#     python3 \
#     wget

# RUN mkdir ../tests/
# COPY tests/ ../tests/

# RUN python3 -m unittest discover -v -s ../tests