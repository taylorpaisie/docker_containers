# Build Dockerfile
FROM ubuntu:focal as builder

RUN apt-get update && apt-get install -y \
    default-jre \
    wget \
    zip \
  && rm -rf /var/lib/apt/lists/*

ENV RDP_ZIP rdp_classifier_2.14.zip
ENV RDP_VERSION 2.14
ENV RDP_DOWNLOAD https://sourceforge.net/projects/rdp-classifier/files/rdp-classifier/$RDP_ZIP/download
ENV RDPPATH /opt/rdp_classifier

RUN wget $RDP_DOWNLOAD -O /tmp/$RDP_ZIP \
  && unzip /tmp/$RDP_ZIP -d /tmp \
  && mv /tmp/${RDP_ZIP%.*} $RDPPATH \
  && rm -rf /tmp/$RDP_ZIP