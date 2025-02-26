#!/bin/bash

output_dir="./PipelineProject_Jerrin_John/assemblies"

mkdir -p "$output_dir"

input_dir="./PipelineProject_Jerrin_John/bowtie2_output"


#Assembles genome for donor 1
spades.py -k 77 -t 4 --only-assembler --pe-1 1 "$input_dir/SRR5660030_mapped_1.fq.gz" --pe-2 1 "$input_dir/SRR5660030_mapped_2.fq.gz" --pe-1 2 "$input_dir/SRR5660033_mapped_1.fq.gz" --pe-2 2 "$input_dir/SRR5660033_mapped_2.fq.gz" -o "$output_dir/Donor1_assembly/"

#Assembles genome for donor 3
spades.py -k 77 -t 4 --only-assembler --pe-1 1 "$input_dir/SRR5660044_mapped_1.fq.gz" --pe-2 1 "$input_dir/SRR5660044_mapped_2.fq.gz" --pe-1 2 "$input_dir/SRR5660045_mapped_1.fq.gz" --pe-2 2 "$input_dir/SRR5660045_mapped_2.fq.gz" -o "$output_dir/Donor3_assembly/"

#Write the spades code to the log file
log_file="./PipelineProject_Jerrin_John/PipelineProject.log"
echo 'output_dir="./PipelineProject_Jerrin_John/assemblies"' >> "$log_file"
echo 'input_dir="./PipelineProject_Jerrin_John/bowtie2_output"' >> "$log_file"
echo 'spades.py -k 77 -t 4 --only-assembler -1 --pe-1 1 "$input_dir/SRR5660044_mapped_1.fq.gz" -pe-2 1 "$input_dir/SRR5660044_mapped_2.fq.gz" --pe-1 2 "$input_dir/SRR5660045_mapped_1.fq.gz" -pe-2 2 "$input_dir/SRR5660045_mapped_2.fq.gz" -o "$output_dir/Donor1_assembly/"' >> "$log_file"
echo 'spades.py -k 77 -t 4 --only-assembler -1 --pe-1 1 "$input_dir/SRR5660044_mapped_1.fq.gz" -pe-2 1 "$input_dir/SRR5660044_mapped_2.fq.gz" --pe-1 2 "$input_dir/SRR5660045_mapped_1.fq.gz" -pe-2 2 "$input_dir/SRR5660045_mapped_2.fq.gz" -o "$output_dir/Donor3_assembly/"' >> "$log_file"

