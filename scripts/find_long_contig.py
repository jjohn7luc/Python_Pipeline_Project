from Bio import SeqIO

#Function to find the longest contig given a fasta file
def get_longest_contig(fasta_file):
    sequences = [] #Save all the contigs into a list
    for record in SeqIO.parse(fasta_file, 'fasta'):
        sequences.append(record) #Add each contig to list

    max_contig = 0 #set starting point for max length
    max_contig_seq = None #Initialize seq to save longest contig

    for contig in sequences: #loop thru list of all contigs
        if len(contig.seq) > max_contig: #if the curr contig length > max contig length
            max_contig = len(contig.seq) #Save new max length
            max_contig_seq = contig #save new longest contig
    
    return max_contig_seq

#FASTA file locations
donor1_fasta = "./PipelineProject_Jerrin_John/assemblies/Donor1_assembly/contigs.fasta"
donor3_fasta = "./PipelineProject_Jerrin_John/assemblies/Donor3_assembly/contigs.fasta"


#Run function to get the longest contig for each donor assembly
Donor1_longest_contig = get_longest_contig(donor1_fasta)
Donor3_longest_contig = get_longest_contig(donor3_fasta)

#Write the longest contigs for each donor into a fasta file
with open("./PipelineProject_Jerrin_John/queries/Donor1_query.fasta", "w") as output_fasta:
    SeqIO.write(Donor1_longest_contig, output_fasta, "fasta")  # Write SeqRecord to file

with open("./PipelineProject_Jerrin_John/queries/Donor3_query.fasta", "w") as output_fasta:
    SeqIO.write(Donor3_longest_contig, output_fasta, "fasta")  # Write SeqRecord to file

