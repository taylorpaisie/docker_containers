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
# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    python3 \
    python3-pip \
    diamond-aligner \
    prodigal


ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${PATH}:${JAVA_HOME}/bin"