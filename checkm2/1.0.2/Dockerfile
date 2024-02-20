# set global variables
ARG CHECKM2_VER="1.0.2"

# build Dockerfile
FROM ubuntu:focal as builder
ARG CHECKM2_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="CheckM2"
LABEL software.version=${CHECKM2_VER}
LABEL description="Rapid assessment of genome bin quality using machine learning."
LABEL website="https://github.com/chklovski/CheckM2"
LABEL license.url="https://github.com/chklovski/CheckM2/blob/main/LICENSE"
LABEL maintainer="Taylor K. Paisie"
LABEL maintainer.email='ltj8@cdc.gov'

ENV DEBIAN_FRONTEND=noninteractive 

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    unzip \
    less \
    automake \
    cmake \
    zlib1g-dev\
    libzstd-dev \
    python3 \
    python3-pip \
    git \
    hmmer \
    prodigal \
    # diamond-aligner \
    build-essential &&\
    apt-get autoclean && rm -rf /var/lib/apt/lists/*

# install checkm2 and its dependencies
RUN pip install --no-cache-dir \
    numpy==1.19.5 \
    scipy==1.8.0 \
    pandas==1.4.0 \
    setuptools \
    requests \
    packaging \
    tqdm \
    scikit-learn==0.23.2 \
    h5py==2.10.0 \
    lightgbm==3.2.1 \
    protobuf==3.20.0 \
    tensorflow==2.2.0

# Install Diamond
RUN wget http://github.com/bbuchfink/diamond/releases/download/v2.0.4/diamond-linux64.tar.gz
RUN tar xzf diamond-linux64.tar.gz

# Clone CheckM2 repository and install
RUN git clone https://github.com/chklovski/checkm2.git &&\
    cd checkm2 &&\
    python3 setup.py install &&\
    cd ..

RUN git clone https://github.com/ncbi/ncbi-cxx-toolkit-public.git
WORKDIR ncbi-cxx-toolkit-public
RUN ./cmake-configure --without-debug --with-projects="objtools/blast/seqdb_reader;objtools/blast/blastdb_format" --with-build-root=build --with-features="-SSE"
WORKDIR build/build
RUN make -j4
RUN cp /opt/diamond/ncbi-cxx-toolkit-public/build/inc/ncbiconf_unix.h /opt/diamond/ncbi-cxx-toolkit-public/include

WORKDIR /opt/diamond/build
RUN cmake -DCMAKE_BUILD_TYPE=Release -DBLAST_INCLUDE_DIR=/opt/diamond/ncbi-cxx-toolkit-public/include -DBLAST_LIBRARY_DIR=/opt/diamond/ncbi-cxx-toolkit-public/build/lib ..
RUN make -j4 && make install

# Running the dockerfile and tests
FROM ubuntu:focal as app
ARG CHECKM2_VER

COPY --from=builder /checkm2/ /checkm2
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/
COPY --from=builder /usr/local/bin/diamond /usr/local/bin/diamond

ENV PATH="${PATH}:/${CHECKM2_PATH}/bin"


# Setting working directory
RUN mkdir data/
WORKDIR /data

# download database and set db in PATH
RUN checkm2 database --download
ENV PATH="${PATH}:/root/databases/CheckM2_database/"

# # run test with internal test data
# # RUN checkm2 testrun --threads 4 \
# #     --database_path /root/databases/CheckM2_database/uniref100.KO.1.dmnd

# ## Test ##
FROM app as test

RUN apt-get update && apt-get install -y \
    python3 \
    wget

RUN mkdir ../tests/
COPY tests/ ../tests/

# RUN python3 -m unittest discover -v -s ../tests

