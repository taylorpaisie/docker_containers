# Set global variables
ARG SEQFU_VER="1.20.3"

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

# Run commands in non-interactive mode
RUN curl https://nim-lang.org/choosenim/init.sh -sSf | sh -s -- -y &&\
    git clone https://github.com/telatin/seqfu2 &&\
    cd seqfu2 &&\
    make &&\
    make test

# Running the dockerfile and tests
FROM ubuntu:focal AS app
ARG SEQFU_VER

COPY --from=builder /usr/ /usr/

# Setting working directory
RUN mkdir /data
WORKDIR /data