from Bio import Seq
from Bio.Seq import Seq
from Bio import Entrez
from Bio import SeqIO
import os
import logging


Entrez.email = "jjohn7@luc.edu"

# Fetch the HCMV genome sequence (NC_006273.2) in GenBank format
accession = "NC_006273.2"
#search nucleotide database for HCMV genome, use genbank format to get CDS information
with Entrez.efetch(db="nuccore", id=accession, rettype="gb", retmode="text") as handle:
    record = SeqIO.read(handle, "genbank")

# Save the GenBank file of HCMV genome locally 
output_file = "./PipelineProject_Jerrin_John/HCMV.gb"
with open(output_file, "w") as out_handle:
    SeqIO.write(record, out_handle, "genbank")


# Load the GenBank file
genbank_file = "./PipelineProject_Jerrin_John/HCMV.gb"

# Define output directory and file path
output_dir = "PipelineProject_Jerrin_John"
output_fasta = os.path.join(output_dir, "HCMV_CDS_DNA.fasta")

CDS_count = 0
# Open output FASTA file
with open(output_fasta, "w") as fasta_out:
    for record in SeqIO.parse(genbank_file, "genbank"): #Parses input genbank file
        for feature in record.features: #loops through all features in genbank record
            if feature.type == "CDS": #if the feature is a CDS
                # Extract protein_id (some may not have it)
                protein_id = feature.qualifiers.get("protein_id")[0] 
                # Extract the DNA sequence of the CDS
                cds_seq = feature.extract(record.seq)  # Gets nucleotide sequence from feature location
                #Add to CDS count
                CDS_count += 1
                # Write to FASTA file
                fasta_out.write(f">{protein_id}\n{cds_seq}\n")

# Count the total number of CDS in the FASTA file
print("The HCMV genome (NC_006273.2) has " + str(CDS_count) +" CDS")






