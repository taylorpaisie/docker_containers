# set global variables
ARG RDP_VER="2.14"

# build Dockerfile
FROM ubuntu:focal as builder
ARG RDP_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="2.14"
LABEL software="RDP Classifier"
LABEL software.version=${RDP_VER}
LABEL description="The RDP Classifier is a naive Bayesian classifier which was developed to provide rapid taxonomic placement based on rRNA sequence data."
LABEL website="https://sourceforge.net/projects/rdp-classifier/"
LABEL license.url="https://github.com/rdpstaff/classifier/blob/master/LICENSE"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='tpaisie91@gmail.com'

# Use an official OpenJDK runtime as a parent image
# Install dependencies
RUN apt-get update && apt-get install -y \
    openjdk-11-jre \
    wget \
    curl \
    unzip \
    ca-certificates

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${PATH}:${JAVA_HOME}/bin"

# Install RDP
ENV RDP_ZIP rdp_classifier_2.14.zip
ENV RDP_DOWNLOAD https://sourceforge.net/projects/rdp-classifier/files/rdp-classifier/rdp_classifier_2.14.zip/download
ENV RDP_PATH /rdp_classifier_2.14

RUN wget $RDP_DOWNLOAD -O /tmp/$RDP_ZIP \
  && unzip /tmp/$RDP_ZIP -d /tmp \
  && mv /tmp/${RDP_ZIP%.*} $RDP_PATH \
  && rm -rf /tmp/$RDP_ZIP \
  && chmod +x ${RDP_PATH}/dist/classifier.jar \
  && ln -s ${RDP_PATH}/dist/classifier.jar /classifier.jar

# ENV PATH="${PATH}:/"






