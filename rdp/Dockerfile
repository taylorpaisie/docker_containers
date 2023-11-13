# Build Dockerfile
FROM ubuntu:focal as builder

RUN apt-get update && apt-get install -y \
    default-jre \
    wget \
    zip \
  && rm -rf /var/lib/apt/lists/*

ENV rdp_zip rdp_classifier_2.14.zip
ENV rdp_version 2.14
ENV rdp_download https://sourceforge.net/projects/rdp-classifier/files/rdp-classifier/$rdp_zip/download
ENV rdp_path /opt/rdp_classifier

RUN wget $rdp_download -O /tmp/$rdp_zip \
  && unzip /tmp/$rdp_zip -d /tmp \
  && mv /tmp/${rdp_zip%.*} $rdp_path \
  && rm -rf /tmp/$rdp_zip