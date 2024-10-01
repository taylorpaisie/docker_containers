# Set global variables
ARG HOCORT_VER="1.1.0"

# Base image
FROM ubuntu:focal AS builder
ARG HOCORT_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="HoCoRT"
LABEL software.version=${HOCORT_VER}
LABEL description="Remove specific organisms from sequencing reads."
LABEL website="https://github.com/ignasrum/hocort"
LABEL license.url="https://github.com/ignasrum/hocort?tab=MIT-1-ov-file#readme"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

ENV DEBIAN_FRONTEND=noninteractive 

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
        build-essential \
        g++ \
        unzip \
        gcc \
        libboost-all-dev \
        libbz2-dev \
        cmake \
        python3 \
        python3-pip \
        git \
        wget \
        zlib1g-dev \
        bowtie2 \
        kraken2 \
        bwa \
        minimap2 \
        samtools \
        bbmap \
        pkg-config \
        liblzma-dev \
        libcurl4-gnutls-dev \
        libssl-dev \
        libgsl-dev && \
        apt-get clean && rm -rf /var/lib/apt/lists/*

# -------------------
# BWA-MEM2 installation
# -------------------
RUN git clone https://github.com/bwa-mem2/bwa-mem2.git && \
    cd bwa-mem2 && \
    git submodule update --init --recursive && \
    make -j$(nproc) && \
    cp bwa-mem2* /usr/local/bin && \
    cd .. && rm -rf bwa-mem2

# -------------------
# HISAT2 installation
# -------------------
RUN wget https://cloud.biohpc.swmed.edu/index.php/s/hisat2-220-source/download -O hisat2.zip && \
    unzip hisat2.zip && \
    cd hisat2-2.2.0 && \
    make -j$(nproc) && \
    cp -r hisat2* /usr/local/bin && \
    cd .. && rm -rf hisat2-2.2.0 hisat2.zip


# -------------------
# SparseHash installation
# -------------------
RUN git clone https://github.com/sparsehash/sparsehash.git && \
    cd sparsehash && \
    ./configure && \
    make && \
    make install && \
    cd .. && rm -rf sparsehash

# -------------------
# SDSL-Lite installation
# -------------------
# Install SDSL-lite
RUN git clone https://github.com/simongog/sdsl-lite.git && \
    cd sdsl-lite && \
    mkdir -p build && cd build && \
    cmake .. && make && make install && \
    cd ../.. && rm -rf sdsl-lite

# -------------------
# Clone and build BTL Bloom filter library (btl_bloomfilter)
# -------------------
# Build and install btl_bloomfilter
RUN git clone https://github.com/bcgsc/btl_bloomfilter.git && \
    cd btl_bloomfilter && \
    chmod +x autogen.sh && \
    ./autogen.sh && \
    ./configure --prefix=/usr/local && \
    make && \
    make install && \
    mkdir -p /usr/local/include/btl_bloomfilter && \
    mv /usr/local/include/*.hpp /usr/local/include/btl_bloomfilter/ && \
    mv vendor /usr/local/include/btl_bloomfilter/

# Clone and build BioBloom (BioBloomMaker and BioBloomCategorizer)
RUN git clone https://github.com/bcgsc/biobloom.git && \
    cd biobloom && \
    ./autogen.sh && \
    ./configure CXXFLAGS="-I/usr/local/include" LDFLAGS="-L/usr/local/lib" && \
    make && \
    make install

# -------------------
# HoCoRT installation
# -------------------
RUN wget https://github.com/ignasrum/hocort/archive/refs/tags/${HOCORT_VER}.tar.gz && \
    tar -xzf ${HOCORT_VER}.tar.gz && \
    rm ${HOCORT_VER}.tar.gz && \
    cd hocort-${HOCORT_VER} && \
    pip3 install .


# Running the dockerfile and tests
FROM ubuntu:focal AS app
ARG HOCORT_VER

COPY --from=builder /usr/ /usr/

# Setting working directory
RUN mkdir /data
WORKDIR /data

# Verify installation
RUN hocort --version && \
    hocort --help
