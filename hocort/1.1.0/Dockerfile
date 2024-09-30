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

# Install CA certificates along with other dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    g++ \
    gcc \
    wget \
    unzip \
    ca-certificates \
    git \
    libtbb-dev \
    libbz2-dev \
    liblzma-dev \
    zlib1g-dev \
    cmake \
    automake \
    autoconf && \
    rm -rf /var/lib/apt/lists/*


# Disable SSL verification (use with caution)
RUN git config --global http.sslVerify false

# Then proceed with cloning sparsehash
RUN git clone https://github.com/sparsehash/sparsehash.git && \
    cd sparsehash && \
    ./configure && \
    make install && \
    export SPARSEHASH_INCLUDE_DIR=$(pwd)/include


# Install sdsl-lite
RUN git clone https://github.com/simongog/sdsl-lite.git && \
    cd sdsl-lite && \
    ./install.sh && \
    export SDSL_INCLUDE_DIR=$(pwd)/include

# Install Biobloomtools from source
RUN git clone https://github.com/bcgsc/biobloom.git && \
    cd biobloom && \
    git submodule update --init && \
    ./autogen.sh && \
    ./configure CXXFLAGS="-I/sdsl-lite/include -I$SPARSEHASH_INCLUDE_DIR" && \
    sleep infinity


# # Install HoCoRT
# RUN git clone https://github.com/ignasrum/hocort.git && \
#     cd hocort && \
#     pip3 install .

# # Running the dockerfile and tests
# FROM ubuntu:focal AS app
# ARG HOCORT_VER

# COPY --from=builder /usr/ /usr/
# COPY --from=builder /opt/ /opt/

# # Setting working directory
# RUN mkdir /data
# WORKDIR /data
