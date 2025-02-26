#!/bin/bash

# Directory containing the FASTQ files and where to put results
data_dir=$DATA_LOC
results_dir="kallisto_results"
index="./PipelineProject_Jerrin_John/index.idx"

# Loop through all the *_1.fastq files in the data directory
for fastq1 in ${data_dir}/*_1.fastq.gz
do
    # Gets the corresponding *_2.fastq file by replacing _1.fastq with _2.fastq
    fastq2="${fastq1/_1.fastq.gz/_2.fastq.gz}"
    
    # Extract the SRR prefix from the file name (assuming the format is SRRxxxxxxx)
    srr=$(basename "$fastq1" "_1.fastq.gz")

    # Define the output directory for kallisto
    output_dir="${results_dir}/${srr}"

    # Create the output directory if it doesn't exist
    mkdir -p "$output_dir"

    # Run kallisto quant
    time kallisto quant -i "$index" -o "$output_dir" -b 10 -t 4 "$fastq1" "$fastq2"
done