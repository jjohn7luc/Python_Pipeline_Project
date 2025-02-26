# Python-Pipeline_Project
COMP 483 COMP BIO PYTHON PIPELINE PROJECT (Jerrin John)

Welcome to the **Python Pipeline Project for Jerrin John**! This repository contains a comprehensive set of Python scripts. The pipeline is intended to automate key steps in the workflow, allowing for more efficient and reproducible results.

## Overview

The goal of this project is to compare HCMV transcriptomes 2- and 6-days post-infection (dpi). 

## Prerequisites

Before using the pipeline, ensure you have the following installed:
- Python
- Biopython and NCBI command line tools
- Kallisto
- Sleuth
- Bowtie2
- SPAdes

This pipeline project focuses specifically on the following transcriptomes:
- SRR5660030 (Donor 1 (2dpi) transcriptome)
- SRR5660033 (Donor 1 (6dpi) transcriptome)
- SRR5660044 (Donor 3 (2dpi) transcriptome)
- SRR5660045 (Donor 3 (6dpi) transcriptome)

The pipeline only runs under the assumption the file names for these transcriptomes are in the following format:
`SRRXXXXXXX_1.fastq.gz / SRRXXXXXXX_1.fastq.gz`
