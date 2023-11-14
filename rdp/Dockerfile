# set global variables
ARG RDP_VER="2.14"

# build Dockerfile
FROM ubuntu:focal as builder
ARG RDP_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="2.14"
LABEL software="RDP"
LABEL software.version=${RDP_VER}
LABEL description="The RDP Classifier is a naive Bayesian classifier which was developed to provide rapid taxonomic placement based on rRNA sequence data."
LABEL website="https://sourceforge.net/projects/rdp-classifier/"
LABEL license.url="https://github.com/rdpstaff/classifier/blob/master/LICENSE"
LABEL maintainer="Taylor K. Paisie"

# Install dependencies
RUN apt-get update && apt-get install -y \
    default-jre \
    wget \
    zip \
  && rm -rf /var/lib/apt/lists/*

# Install RDP
RUN RDP_ZIP rdp_classifier_2.14.zip
ENV RDP_VERSION 2.14
ENV RDP_DOWNLOAD https://sourceforge.net/projects/rdp-classifier/files/rdp-classifier/$RDP_ZIP/download
ENV RDP_PATH /opt/rdp_classifier
RUN wget $RDP_DOWNLOAD -O /tmp/$RDP_ZIP \
  && unzip /tmp/$RDP_ZIP -d /tmp \
  && mv /tmp/${RDP_ZIP%.*} $RDP_PATH \
  && rm -rf /tmp/$RDP_ZIP


# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/

RUN mkdir data/
WORKDIR /data

# Run Dockerfile
