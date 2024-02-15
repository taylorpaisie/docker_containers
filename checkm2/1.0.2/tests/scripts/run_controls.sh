#!/bin/bash

# Download test data
wget -nv https://github.com/taylorpaisie/docker_containers/blob/main/checkm2/1.0.2/GCF_030010175.1_ASM3001017v1_genomic.fna.gz -O burk_wgs_test.fa.gz
wget -nv https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/rdp/2.14/16S_rRNA_gene.Burkholderia_pseudomallei.2002721184.AY305776.1.fasta -O 16S_test.fa
wget -nv https://github.com/taylorpaisie/docker_containers/blob/main/checkm2/1.0.2/neg_control_test.fna -O neg_control_test.fna

# Get taxonomic assignments for your data
checkm2 predict --input burk_wgs_test.fa \
    16S_test.fa neg_control_test.fna \
    --output-directory test_output/

# run checksum on files
sha256sum burk_wgs_test.fa > burk_wgs_test_checksum.txt
