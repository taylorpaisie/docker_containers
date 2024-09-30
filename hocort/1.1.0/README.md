# HoCoRT

Main tool: [HoCoRT](https://github.com/ignasrum/hocort)
  
Code repository: https://github.com/ignasrum/hocort

Basic information on how to use this tool:
- executable: |
```
  · count [cnt]         : count FASTA/FASTQ reads, pair-end aware
  · deinterleave [dei]  : deinterleave FASTQ
  · derep [der]         : feature-rich dereplication of FASTA/FASTQ files
  · interleave [ilv]    : interleave FASTQ pair ends
  · lanes [mrl]         : merge Illumina lanes
  · list [lst]          : print sequences from a list of names
  · metadata [met]      : print a table of FASTQ reads (mapping files)
  · sort [srt]          : sort sequences by size (uniques)
  · stats [st]          : statistics on sequence lengths

  · cat                 : concatenate FASTA/FASTQ files
  · grep                : select sequences with patterns
  · head                : print first sequences
  · rc                  : reverse complement strings or files
  · tab                 : tabulate reads to TSV (and viceversa)
  · tail                : view last sequences
  · view                : view sequences with colored quality and oligo matches
```

- help: `hocort --help`
- version: `hocort --version`
- description: | 
> A general-purpose program to manipulate and parse information from FASTA/FASTQ files, supporting gzipped input files. 

  
Full documentation: https://github.com/ignasrum/hocort/wiki


# Testing HoCoRT analysis
```
hocort check \
      --deep \
      --verbose \
      /root/HoCoRT2-1.20.3/data/tests/sample1_R1.fq \
      /root/HoCoRT2-1.20.3/data/tests/sample1_R2.fq
```