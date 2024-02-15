#!/bin/bash

# Download test data
wget -nv https://github.com/taylorpaisie/docker_containers/blob/main/checkm2/1.0.2/TEST1.fasta -O TEST1.fasta
wget -nv https://github.com/taylorpaisie/docker_containers/blob/main/checkm2/1.0.2/TEST2.fasta -O TEST2.fasta
wget -nv https://github.com/taylorpaisie/docker_containers/blob/main/checkm2/1.0.2/TEST3.fasta -O TEST3.fasta

# Get taxonomic assignments for your data
checkm2 predict --threads 30 --input <folder_with_bins> --output-directory <output_folder> 


# run checksum on files
sha256sum TEST1.fasta > TEST1_checksum.txt
sha256sum TEST2.fasta > TEST2_checksum.txt
sha256sum TEST3.fasta > TEST3_checksum.txt