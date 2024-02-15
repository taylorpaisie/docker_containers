# set global variables
ARG CHECKM2_VER="2.14"

# build Dockerfile
FROM ubuntu:focal as builder
ARG RDP_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="CheckM2"
LABEL software.version=${RDP_VER}
LABEL description="The RDP Classifier is a naive Bayesian classifier which was developed to provide rapid taxonomic placement based on rRNA sequence data."
LABEL website="https://sourceforge.net/projects/rdp-classifier/"
LABEL license.url="https://github.com/rdpstaff/classifier/blob/master/LICENSE"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

ENV DEBIAN_FRONTEND=noninteractive 

# Install dependencies
RUN apt-get update && apt-get install -y \
    openjdk-11-jre \
    wget \
    curl \
    unzip 

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${PATH}:${JAVA_HOME}/bin"