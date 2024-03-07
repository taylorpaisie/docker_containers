# Centrifuge

This image implements:
* [Centrifuge v1.0.4.1](ttps://github.com/DaehwanKimLab/centrifuge)

It can be accessed at [docker hub](https://hub.docker.com/u/tpaisie).

Centrifuge is a novel microbial classification engine that enables rapid, accurate and sensitive labeling of reads and quantification of species on desktop computers. The system uses a novel indexing scheme based on the Burrows-Wheeler transform (BWT) and the Ferragina-Manzini (FM) index, optimized specifically for the metagenomic classification problem. Centrifuge requires a relatively small index (4.7 GB for all complete bacterial and viral genomes plus the human genome) and classifies sequences at very high speed, allowing it to process the millions of reads from a typical high-throughput DNA sequencing run within a few minutes. Together these advances enable timely and accurate analysis of large metagenomics data sets on conventional desktop computers.

The Centrifuge hompage is http://www.ccb.jhu.edu/software/centrifuge

The Centrifuge paper is available at https://genome.cshlp.org/content/26/12/1721

The Centrifuge poster is available at http://www.ccb.jhu.edu/people/infphilo/data/Centrifuge-poster.pdf


## Centrifuge database download and index building

Centrifuge indexes can be built with arbritary sequences. Standard choices are all of the complete bacterial and viral genomes, or using the sequences that are part of the BLAST nt database. Centrifuge always needs the nodes.dmp file from the NCBI taxonomy dump to build the taxonomy tree, as well as a sequence ID to taxonomy ID map. The map is a tab-separated file with the sequence ID to taxonomy ID map.


### Building the Centrifuge indices:
```
# Building the indices using the Centrifuge test dataset:
centrifuge-build --conversion-table \
    ../centrifuge-1.0.4.1/example/reference/gi_to_tid.dmp \
    --taxonomy-tree ../centrifuge-1.0.4.1/example/reference/nodes.dmp \
    --name-table ../centrifuge-1.0.4.1/example/reference/names.dmp \
    ../centrifuge-1.0.4.1/example/reference/test.fa test

# Running Centrifuge on the built-in test dataset 
centrifuge -f -x test ../centrifuge-1.0.4.1/example/reads/input.fa
```

#### Running Centrifuge with pre-built NCBI database and test dataset
```
# Download positive and negative control test data
wget -nv --no-check-certificate https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_wgs.fa -O burk_wgs_pos_ctrl.fa
wget -nv --no-check-certificate https://raw.githubusercontent.com/taylorpaisie/docker_containers/main/checkm2/1.0.2/burk_16S.fa -O burk_16S_neg_ctrl.fa

```