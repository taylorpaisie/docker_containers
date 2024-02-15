#!/bin/bash

# Download test data
# wget -nv https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/accession/GCF_030010175.1/download?include_annotation_type=GENOME_FASTA -O burk_wgs_test.fa

# Get taxonomic assignments for your data
checkm2 predict --input burk_wgs_test.fa --output-directory /data

# run checksum on files
sha256sum burk_wgs_test.fa > burk_wgs_test_checksum.txt
