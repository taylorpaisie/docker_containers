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

# Install required dependencies, including Boost and other build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    g++ \
    gcc \
    libc6-dev \
    libstdc++6 \
    libtool \
    pkg-config \
    zlib1g-dev \
    cmake \
    wget \
    git \
    ca-certificates \
    libtbb-dev \
    libbz2-dev \
    liblzma-dev \
    automake \
    autoconf \
    libboost-all-dev \
    lzma \
    liblzma-dev \
    python3 \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Disable SSL verification for git
RUN git config --global http.sslVerify false

# Install SparseHash
RUN git clone https://github.com/sparsehash/sparsehash.git && \
    cd sparsehash && \
    ./configure && \
    make && \
    make install

# Install SDSL-lite
RUN git clone https://github.com/simongog/sdsl-lite.git && \
    cd sdsl-lite && \
    ./install.sh && \
    cp /root/lib/libsdsl.a /usr/local/lib/ && \
    ldconfig

# Install BioBloomTools
RUN git clone https://github.com/bcgsc/biobloom.git && \
    cd biobloom && \
    git submodule update --init && \
    ./autogen.sh && \
    ./configure CXXFLAGS="-I/sdsl-lite/include -I/usr/local/include/sparsehash -Wno-error=ignored-qualifiers" LDFLAGS="-L/usr/local/lib" && \
    make && \
    make install

# Install HoCoRT
RUN git clone https://github.com/ignasrum/hocort.git && \
    cd hocort && \
    pip3 install .

# Command to keep the container alive for further inspection/debugging
CMD ["sleep", "infinity"]


# Running the dockerfile and tests
FROM ubuntu:focal AS app
ARG HOCORT_VER

COPY --from=builder /usr/ /usr/
COPY --from=builder /opt/ /opt/

# Setting working directory
RUN mkdir /data
WORKDIR /data
