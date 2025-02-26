#!/bin/bash

#directory to store blast results and db
mkdir -p ./PipelineProject_Jerrin_John/blast_results

#Go into this directory to download genome file
cd ./PipelineProject_Jerrin_John/blast_results

#Download genome file
datasets download virus genome taxon Betaherpesvirinae --refseq --include genome

unzip ncbi_dataset.zip

#Move and rename genome file
mv ncbi_dataset/data/genomic.fna ./Betaherpesvirinae.fna

#Make local database
makeblastdb -in Betaherpesvirinae.fna -out Betaherpesvirinae -title Betaherpesvirinae -dbtype nucl


cd ..
cd ..

#blast donor 1 
blastn -query ./PipelineProject_Jerrin_John/queries/Donor1_query.fasta -db ./PipelineProject_Jerrin_John/blast_results/Betaherpesvirinae -out ./PipelineProject_Jerrin_John/donor1_blast_results.txt -max_hsps 1  -max_target_seqs 10 -outfmt "6  sacc pident length qstart qend sstart send bitscore evalue stitle"

#blast donor 3
blastn -query ./PipelineProject_Jerrin_John/queries/Donor3_query.fasta -db ./PipelineProject_Jerrin_John/blast_results/Betaherpesvirinae -out ./PipelineProject_Jerrin_John/donor3_blast_results.txt -max_hsps 1  -max_target_seqs 10 -outfmt "6  sacc pident length qstart qend sstart send bitscore evalue stitle"