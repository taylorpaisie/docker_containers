# set global variables
ARG rdp_ver="2.14"

# build Dockerfile
FROM ubuntu:focal as builder
ARG rdp_ver

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="2.14"
LABEL software="RDP Classifier"
LABEL software.version=${rdp_ver}
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
ENV rdp_zip rdp_classifier_2.14.zip
ENV rdp_version 2.14
ENV rdp_download https://sourceforge.net/projects/rdp-classifier/files/rdp-classifier/$rdp_zip/download
ENV rdp_path /opt/rdp_classifier
RUN wget $rdp_download -O /tmp/$rdp_zip \
  && unzip /tmp/$rdp_zip -d /tmp \
  && mv /tmp/${rdp_zip%.*} $rdp_path \
  && rm -rf /tmp/$rdp_zip


# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/

RUN mkdir data/
WORKDIR /data

# Run Dockerfile
