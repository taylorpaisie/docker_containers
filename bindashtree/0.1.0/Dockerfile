# Set global variables
ARG BINDASHTREE_VER="0.1.0"

# Stage 1: Build stage
FROM ubuntu:focal AS builder

# Set version argument
ARG BINDASHTREE_VER

# Update package manager and install necessary tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    build-essential \
    gcc \
    pkg-config \
    libssl-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Rust and Cargo
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y || \
    (wget https://sh.rustup.rs -O rustup-init.sh && sh rustup-init.sh -y) && \
    echo "source $HOME/.cargo/env" >> ~/.bashrc && \
    . $HOME/.cargo/env

# Download, extract, and build bindashtree
RUN wget https://github.com/jianshu93/bindashtree/archive/refs/tags/v${BINDASHTREE_VER}.tar.gz && \
    tar -xzvf v${BINDASHTREE_VER}.tar.gz && \
    cd bindashtree-${BINDASHTREE_VER} && \
    cargo build --release

# Stage 2: Final image
FROM ubuntu:focal AS app

# Labels for metadata
LABEL base.image="ubuntu:focal" \
      dockerfile.version="1" \
      software="bindashtree" \
      software.version="${BINDASHTREE_VER}" \
      description="Binwise Densified MinHash and Rapid Neighbor-joining Tree Construction for microbial genomes." \
      website="https://github.com/jianshu93/bindashtree" \
      license.url="https://github.com/jianshu93/bindashtree?tab=MIT-1-ov-file#readme" \
      maintainer="Taylor K. Paisie" \
      maintainer.email="ltj8@cdc.gov"

# Copy built binaries from builder stage
COPY --from=builder /bindashtree-${BINDASHTREE_VER}/target/release/bindashtree /usr/local/bin/

# Set default command
CMD ["bindashtree", "-h"]


# Optional stage: Test data
# FROM app AS test

# WORKDIR /data/test

# # Prepare testing database
# RUN mkdir -p db_tests && \
#     gzip -d /CAT/tests/data/prepare/small.fa.gz && \
#     CAT prepare --db_fasta /CAT/tests/data/prepare/small.fa \
#     --acc2tax /CAT/tests/data/prepare/prot2acc.txt \
#     --names /CAT/tests/data/prepare/names.dmp \
#     --nodes /CAT/tests/data/prepare/nodes.dmp \
#     --db_dir db_tests/

# # Run CAT test
# RUN CAT contigs -c /CAT/tests/data/contigs/small_contigs.fa \
#     -d db_tests/db/ -t db_tests/tax/

# WORKDIR /data
