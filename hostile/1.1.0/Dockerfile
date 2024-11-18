# Set global variables
ARG HOSTILE_VER="1.1.0"

# Stage 1: Build Dockerfile
FROM ubuntu:focal AS builder
ARG HOSTILE_VER

# Metadata
LABEL base.image="ubuntu:focal" 
LABEL dockerfile.version="1" 
LABEL software="hostile"
LABEL software.version="${HOSTILE_VER}"
LABEL description="Precise host read removal."
LABEL website="https://github.com/bede/hostile"
LABEL license.url="https://github.com/bede/hostile?tab=MIT-1-ov-file#readme"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email="ltj8@cdc.gov"


RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    build-essential \
    zlib1g-dev \
    curl \
    python3 \
    python3-pip \
    git \
    samtools \
    minimap2 \
    bowtie2 \
    gawk \
    bedtools \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/*


# Install HoCoRT
RUN wget https://github.com/bede/hostile/archive/refs/tags/${HOSTILE_VER}.tar.gz && \
    tar -xzvf ${HOSTILE_VER}.tar.gz && cd hostile-${HOSTILE_VER} && \
    rm -rf hostile-${HOSTILE_VER}

# Second stage: Create the final app image
FROM ubuntu:20.04 AS app
ARG HOSTILE_VER

COPY --from=builder /usr/ /usr/

# Set up working directory
WORKDIR /data

# # Verify installation
# RUN hocort --version

# # Optional: Test stage
# FROM app AS test

# RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl && \
#     mkdir test && curl -L -o test/genome.fna https://raw.githubusercontent.com/ignasrum/hocort/main/tests/test_data/fasta/genome.fna && \
#     hocort index bowtie2 --input test/genome.fna --output test/hocort_test && \
#     rm -rf /var/lib/apt/lists/*


