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

# Install dependencies
RUN apt-get update && apt-get install -y \
    default-jre \
    wget \
    curl \
    unzip 

# Install RDP
ENV RDP_ZIP rdp_classifier_2.14.zip
ENV RDP_DOWNLOAD https://sourceforge.net/projects/rdp-classifier/files/rdp-classifier/rdp_classifier_2.14.zip/download
ENV RDP_PATH /rdp_classifier

RUN wget $RDP_DOWNLOAD -O /tmp/$RDP_ZIP \
  && unzip /tmp/$RDP_ZIP -d /tmp \
  && mv /tmp/${RDP_ZIP%.*} $RDP_PATH \
  && rm -rf /tmp/$RDP_ZIP 
  # && chmod +x /${RDP_PATH}/dist/classifier.jar

# need to get this to work in the working directory
# ENV PATH="${PATH}:/Trimmomatic-${TRIMMOMATIC_VER}/"
ENV PATH="${PATH}:/${RDP_PATH}/dist/"
# ENV JAVA_HOME=/usr/bin/java
# ENV PATH="${RDP_PATH}/dist/"

# ENV PATH="${PATH}:/Trimmomatic-${TRIMMOMATIC_VER}/"

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/
# create /data directory and set as working directory
RUN mkdir /data
WORKDIR /data

# FROM app as test
# ARG TRIMMOMATIC_VER

