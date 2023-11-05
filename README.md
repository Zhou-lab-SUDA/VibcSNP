# VibcSNP
SNP barcode decoding program for *Vibrio cholerae*

## Installation
VibcSNP spell was devoloped and tested in Python 3.9.0, and requires a several modules:
~~~~~~~~~~
fastANI
samtools
bcftools
minimap2
~~~~~~~~~~

Enjoy a cup of coffee while installing these packages using commands below:
~~~~~~~~~~
pip install fastani minimap2
conda install -c bio-conda samtools bcftools minimap2
FYI: some version of pandas might not be support DataFrame.append() any more.
~~~~~~~~~~

## Quick Start (with example)
VibcSNP requires a sequence file(in fasta format), you can simply submit your genome following -q/--query flag:
~~~~~~~~~~
python  VibcSNP.py -q vc_example[you can replace it with your own genome]
~~~~~~~~~~
The first step of VibcSNP is to check the species of the genome using 95 of average nucleotide identity against the reference genome of *Vibrio cholerae* N16961. 

If average nucleotide identity is lower than threshold, VibcSNP will exit.
~~~~~~~~~~
Try a non-Vibrio cholerae genome with command below:
python  VibcSNP.py -q non_vc_example
~~~~~~~~~~
If genome is likely to be *Vibrio cholerae*, VibcSNP will print the value of average nucleotide identity.

The second step of VibcSNP is to detect a series of specific SNPs from monophyletic groups we have identified.
~~~~~~~~~~
python  VibcSNP.py -q vc_example
~~~~~~~~~~
Command above will print such information:

yyyy-mm-dd time     ---Species Identification---
yyyy-mm-dd time      Input genome is from species vibrio cholerae
yyyy-mm-dd time     Average Nucleotide Identity: 98.1241
yyyy-mm-dd time     ---SNP detection---
yyyy-mm-dd time     SNP lineage: 3.4.8
yyyy-mm-dd time     ---Done---
