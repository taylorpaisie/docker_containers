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


# Install basic dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    python3.10 \
    python3.10-distutils \
    build-essential \
    wget \
    curl \
    unzip \
    samtools \
    minimap2 \
    bedtools \
    gawk && \
    update-ca-certificates && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install pip for Python 3.10
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python3.10 get-pip.py && \
    rm get-pip.py && \
    pip install setuptools && \
    ln -sf /usr/bin/python3.10 /usr/bin/python3 && \
    ln -sf /usr/local/bin/pip /usr/bin/pip

# Install bowtie2
RUN wget https://github.com/BenLangmead/bowtie2/releases/download/v2.5.1/bowtie2-2.5.1-linux-x86_64.zip && \
    unzip bowtie2-2.5.1-linux-x86_64.zip && \
    mv bowtie2-2.5.1-linux-x86_64 /usr/local/bin/bowtie2 && \
    ln -s /usr/local/bin/bowtie2/bowtie2 /usr/bin/bowtie2 && \
    rm bowtie2-2.5.1-linux-x86_64.zip

# Install hostile
RUN wget https://github.com/bede/hostile/archive/refs/tags/${HOSTILE_VER}.tar.gz && \
    tar -xzvf ${HOSTILE_VER}.tar.gz && \
    cd hostile-${HOSTILE_VER} && \
    pip install . && \
    cd .. && rm -rf ${HOSTILE_VER}.tar.gz


# Second stage: Create the final app image
FROM ubuntu:focal AS app 
ARG HOSTILE_VER

# Copy dependencies and hostile tool
COPY --from=builder /usr/ /usr/

# Ensure CA certificates are updated
RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates

# Download test data (optional)
FROM app AS test

WORKDIR /data/test

RUN wget https://github.com/bacterial-genomics/test-datasets/raw/assembly/test_data/test_miniburk_R1.fastq.gz \
        --no-check-certificate && \
    wget https://github.com/bacterial-genomics/test-datasets/raw/assembly/test_data/test_miniburk_R2.fastq.gz \
        --no-check-certificate && \
    hostile fetch && \
    hostile clean --fastq1 test_miniburk_R1.fastq.gz --fastq2 test_miniburk_R2.fastq.gz

WORKDIR /data



