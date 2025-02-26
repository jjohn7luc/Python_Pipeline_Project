# Python-Pipeline_Project
COMP 483 COMP BIO PYTHON PIPELINE PROJECT (Jerrin John)

Welcome to the **Python Pipeline Project for Jerrin John**! This repository contains a comprehensive set of Python, bash, and R scripts. The pipeline is intended to automate key steps in the workflow, allowing for more efficient and reproducible results.

## Overview

The goal of this project is to compare HCMV transcriptomes 2- and 6-days post-infection (dpi) by using tools which allow us to efficiently quantify, align, assemble, and annotate the HCMV transcriptomes.

## Prerequisites

Before using the pipeline, ensure you have the following installed:
- Python
- R
- Biopython (Python Package)
- NCBI command line tools (blast, datasets, efetch, etc)
- Kallisto
- Sleuth (R package)
- Bowtie2
- SPAdes

This pipeline project focuses specifically on the following transcriptomes:
- SRR5660030 (Donor 1 (2dpi) transcriptome)
- SRR5660033 (Donor 1 (6dpi) transcriptome)
- SRR5660044 (Donor 3 (2dpi) transcriptome)
- SRR5660045 (Donor 3 (6dpi) transcriptome)

The pipeline only runs under the assumption the file names for these transcriptomes are in the following format:
`SRRXXXXXXX_1.fastq.gz / SRRXXXXXXX_1.fastq.gz`

The following command will allow you to download the transcriptomes if you do not have it already and write them into a directory named `/full_data`.
```bash
./HCMV_donor_download
```

## Sample Data

A condensed version of the transcriptomes, which contains only 10,000 reads per fastq file is available for use in the `data` directory provided in this repo. This dataset is ideal for testing the entire pipeline quickly.

## Running the Pipeline

A walkthrough of the pipeline using the sample data.

### The Wrapper Script

Once the all the necessary software and files are obtained, all that is needed to run the pipeline is the name of the directory where the transcriptomes are located. The following provides the command required to run the pipeline using the sample data as an example. It will run a python wrapper script taking in the directory name as the input.
```bash
python wrapper_script.py --input data
```
You would change `data` to be the name of directory where your transcriptomes are located. 

### Results
The script will create a new directory, `PipelineProject_Jerrin_John`. **Most outputs** from the softwares used, like Kallisto, Bowtie2, etc., will be written into this directory. All the results required for the project are written into the `PipelineProject.log file`, written in the required format. 
The results with the requested output from running the pipeline with **all input reads** is in the `PipelineProject.log file` already included in this repository. 

