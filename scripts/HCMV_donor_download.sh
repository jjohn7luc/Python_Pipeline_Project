#!/bin/bash
#Script to download the necessary transcriptomes
mkdir -p data

cd data

wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR5660030/SRR5660030 #Donor 1 (2dpi) transcriptome
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR5660033/SRR5660033 #Donor 1 (6dpi) transcriptome
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR5660044/SRR5660044 #Donor 3 (2dpi) transcriptome
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR5660045/SRR5660045 #Donor 3 (6dpi) transcriptome

#Convert the SRR files to paired end fastq files
fastq-dump --split-files --gzip SRR5660030
fastq-dump --split-files --gzip SRR5660033
fastq-dump --split-files --gzip SRR5660044
fastq-dump --split-files --gzip SRR5660045

#Remove the SRR files
find . ! -name "*.fastq.gz" -type f -delete

cd ..
