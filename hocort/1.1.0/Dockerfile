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
    # samtools \
    # bowtie2 \
    # hisat2 \
    # bbmap \
    # minimap2 \
    && rm -rf /var/lib/apt/lists/*


# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh && \
    bash /miniconda.sh -b -p /opt/conda && \
    rm /miniconda.sh && \
    /opt/conda/bin/conda clean -t -i -p -y && \
    ln -s /opt/conda/bin/conda /usr/local/bin/conda

# Update conda and install TBB
RUN conda update -n base -c defaults conda && \
    # conda install -c conda-forge tbb==2020.2 &&\
    # conda install -c bioconda -c conda-forge biobloomtools &&\
    conda create -n hocort -c conda-forge -c bioconda hocort


# Install HoCoRT
# RUN wget https://raw.githubusercontent.com/ignasrum/hocort/main/install.sh && \ 
#     wget https://raw.githubusercontent.com/ignasrum/hocort/main/environment.yml && \
#     bash ./install.sh && \
#     /opt/conda/bin/conda activate hocort

# Running the dockerfile and tests
FROM ubuntu:focal AS app
ARG HOCORT_VER

COPY --from=builder /usr/ /usr/

# Setting working directory
RUN mkdir /data
WORKDIR /data
