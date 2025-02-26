#!/bin/bash

mkdir ./PipelineProject_Jerrin_John/bowtie2_index

cd ./PipelineProject_Jerrin_John/bowtie2_index

#Download HCMV genome 
datasets download genome accession GCF_000845245.1 --include gff3,rna,cds,protein,genome,seq-report

#Unzip dataset
unzip ncbi_dataset.zip

#Make directory to store index
mkdir index
#Build bowtie index
bowtie2-build ncbi_dataset/data/GCF_000845245.1/GCF_000845245.1_ViralProj14559_genomic.fna ./index/HCMV

#Store index and data locations
data_dir=$DATA_LOC
index="./PipelineProject_Jerrin_John/bowtie2_index/index/HCMV"

cd ..
cd ..

# Define the output directory
output_dir="./PipelineProject_Jerrin_John/bowtie2_output"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

log_file="./PipelineProject_Jerrin_John/PipelineProject.log"


for fastq1 in ${data_dir}/*_1.fastq.gz
do
    #Gets the paired fastq file name (_2.fastq)
    fastq2="${fastq1/_1.fastq.gz/_2.fastq.gz}"
    #Gets the base name (SRRXXXXX)
    srr=$(basename "$fastq1" "_1.fastq.gz")

    # Count reads before mapping
    reads_before=$(zgrep -c "^@" "$fastq1")

    # Run Bowtie2, keeping only mapped reads
    bowtie2 --quiet -x ./index/HCMV -1 "$fastq1" -2 "$fastq2" -S "$output_dir/$srr.sam" \
        --al-conc-gz "$output_dir/${srr}_mapped_%.fq.gz" 

    # Count mapped reads using presence of @
    reads_after=$(zgrep -c "^@" "$output_dir/${srr}_mapped_1.fq.gz")

    # Log read counts depending on SRR
    if [ $srr = "SRR5660030" ]; then
    echo "Donor 1 (2dpi) had $reads_before read pairs before Bowtie2 filtering and $reads_after read pairs after" >> "$log_file"
    elif [ $srr = "SRR5660033" ]; then
    echo "Donor 1 (6dpi) had $reads_before read pairs before Bowtie2 filtering and $reads_after read pairs after" >> "$log_file"
    elif [ $srr = "SRR5660044" ]; then
    echo "Donor 3 (2dpi) had $reads_before read pairs before Bowtie2 filtering and $reads_after read pairs after" >> "$log_file"
    elif [ $srr = "SRR5660045" ]; then
    echo "Donor 3 (6dpi) had $reads_before read pairs before Bowtie2 filtering and $reads_after read pairs after" >> "$log_file"
    fi

done




