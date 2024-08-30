# Set global variables
ARG HOCORT_VER="1.1.0"

# Build Dockerfile
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

# Install required dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    python3-pip \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh && \
    bash /miniconda.sh -b -p /opt/conda && \
    rm /miniconda.sh && \
    /opt/conda/bin/conda clean -t -i -p -y && \
    ln -s /opt/conda/bin/conda /usr/local/bin/conda

# Initialize Conda for bash
RUN /opt/conda/bin/conda init bash

# Update conda, install git, TBB, and switch to the classic solver
RUN conda update -n base -c defaults conda && \
    conda config --set solver classic && \
    conda install -c conda-forge tbb==2020.2 git && \
    conda install -c bioconda -c conda-forge biobloomtools

# Install HoCoRT
RUN wget https://raw.githubusercontent.com/ignasrum/hocort/main/install.sh && \
    wget https://raw.githubusercontent.com/ignasrum/hocort/main/environment.yml && \
    sed -i '/conda activate hocort/a conda install -n hocort -c conda-forge git' install.sh && \
    bash ./install.sh

# Use bash shell to activate the conda environment correctly
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate hocort" >> ~/.bashrc

# Running the dockerfile and tests
FROM ubuntu:focal AS app
ARG HOCORT_VER

COPY --from=builder /usr/ /usr/

# Setting working directory
RUN mkdir /data
WORKDIR /data
