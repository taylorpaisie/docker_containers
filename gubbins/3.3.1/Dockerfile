FROM ubuntu:focal as app

ARG GUBBINS_VER="3.3.1"

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Gubbins"
LABEL software.version=${GUBBINS_VER}}
LABEL description="Gubbins - Genealogies Unbiased by recomBinations in Nucleotide Sequences"
LABEL website="https://github.com/nickjcroucher/gubbins/"
LABEL license.url="https://github.com/nickjcroucher/gubbins/blob/master/LICENSE"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

ENV DEBIAN_FRONTEND=noninteractive 

#libtool autoconf-archive automake pkg-config check pytest
# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    git \
    libtool \
    autoconf-archive \
    automake \
    pkg-config \
    check \
    python3 \
    python3-pip \
    python3-distutils \
    ca-certificates

# Install Python dependencies
RUN pip3 install \
  pytest \
  pytest-cov \
  biopython==1.78 \
  multiprocess==0.70.11 \
  scipy==1.6.0 \
  numpy==1.19.5 \
  dendropy==4.5.1

RUN apt-get update && apt-get install -y \
  gubbins

# install Gubbins from github; make /data
# RUN git clone https://github.com/nickjcroucher/gubbins.git && \
#   cd gubbins &&\
#   autoreconf -i &&\
#   chmod +x configure &&\
#   ./configure &&\
#   make &&\
#   sudo make install &&\
#   cd python &&\
#   python3 -m pip install . &&\
#   mkdir /data

# set PATH and locale settings for singularity
ENV LC_ALL=C.UTF-8 \
    PATH="${PATH}:/gubbins/bin"

WORKDIR /data

# test layer
# FROM app as test

# print version and run the supplied test flag
# RUN spades.py --version && spades.py --test && spades.py --help



