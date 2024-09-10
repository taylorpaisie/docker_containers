# Set global variables
ARG SEQFU_VER="1.22.0"

# Build Dockerfile
FROM ubuntu:focal AS builder
ARG SEQFU_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="SeqFu"
LABEL software.version=${SEQFU_VER}
LABEL description="A general-purpose program to manipulate and parse information from FASTA/FASTQ files, supporting gzipped input files."
LABEL website="https://github.com/telatin/seqfu2"
LABEL license.url="https://github.com/telatin/seqfu2?tab=GPL-3.0-1-ov-file#readme"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

# Set non-interactive frontend
ENV DEBIAN_FRONTEND=noninteractive 

# Set PATH globally to include Nimble binaries
ENV PATH="/root/.nimble/bin:${PATH}"

# Install required dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    build-essential \
    zlib1g-dev \
    curl \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /root
WORKDIR /root

# Run commands in non-interactive mode
RUN curl https://nim-lang.org/choosenim/init.sh -sSf | sh -s -- -y &&\
    git clone https://github.com/telatin/seqfu2 &&\
    cd seqfu2 &&\
    make &&\
    make test

# Debugging: List files to check where seqfu binary is located
RUN find /root/seqfu2 -type f

# Copy the built binary to a location in the PATH
RUN cp /root/seqfu2/bin/seqfu /usr/local/bin/seqfu

# Final image
FROM ubuntu:focal AS app
ARG SEQFU_VER

# Copy the necessary files from the builder
COPY --from=builder /usr/local/bin/seqfu /usr/local/bin/seqfu
COPY --from=builder /root/seqfu2/data/tests /root/seqfu2/data/tests

# Setting working directory
RUN mkdir /data
WORKDIR /data

RUN seqfu --version &&\
    seqfu --help

# Running seqfu on test controls
# FROM app as test

# RUN apt-get update && apt-get install -y \
#     python3 \
#     wget

# RUN mkdir ../tests/
# COPY tests/ ../tests/
# RUN python3 -m unittest discover -v -s ../tests