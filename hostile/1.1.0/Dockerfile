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





