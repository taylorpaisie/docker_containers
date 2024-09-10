#!/bin/bash

# Download test data
wget -nv --no-check-certificate https://github.com/bacterial-genomics/wf-paired-end-illumina-assembly/blob/main/assets/test_data/test_R1.fastq.gz -O test_R1.fastq.gz
wget -nv --no-check-certificate https://github.com/bacterial-genomics/wf-paired-end-illumina-assembly/blob/main/assets/test_data/test_R2.fastq.gz -O test_R2.fastq.gz

# Get taxonomic assignments for your data
seqfu check \
      --deep \
      --verbose \
      test_R1.fastq.gz test_R2.fastq.gz

# run checksum on files
# sha256sum burk_wgs_pos_ctrl.fa > burk_wgs_checksum.txt
# sha256sum burk_16S_neg_ctrl.fa > burk_16S_checksum.txt
# sha256sum tests_output/quality_report.tsv > quality_report_checksum.txt