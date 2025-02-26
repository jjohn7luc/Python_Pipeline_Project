import os 
import logging
import argparse
import sys

#function to parse command line arguments
def check_arg(args=None):
    parser = argparse.ArgumentParser(description='input location of data directory')
    parser.add_argument('-i', '--input', help='path to input data',required ='True') #add command line arguement for input file
    return parser.parse_args(args)

#retrieve command line arguments and assign to variables
args = check_arg(sys.argv[1:])
infile = args.input #store input file path

# Set the environment variable for the shell script
os.environ["DATA_LOC"] = infile

# Command to create a directory
os.system('mkdir PipelineProject_Jerrin_John')

#Create the Log File
logging.basicConfig(filename="PipelineProject_Jerrin_John/PipelineProject.log", level=logging.INFO)

#Script to create a fasta file and count the total CDS in HCMV genome
os.system("python3 ./scripts/step2.py >> PipelineProject_Jerrin_John/PipelineProject.log 2>&1; echo '' >> PipelineProject_Jerrin_John/PipelineProject.log")

#Create Kallisto Index
os.system("kallisto index -i PipelineProject_Jerrin_John/index.idx PipelineProject_Jerrin_John/HCMV_CDS_DNA.fasta")

#Create a directory to save Kallisto results
os.sysem("mkdir PipelineProject_Jerrin_John/results")

#Make kallisto quantification script active
os.system("chmod +x ./scripts/kallistoscript.sh")

#Run shell script to perform Kallisto Quanitification
os.system("./scripts/kallistoscript.sh")

#Run script to get TPM info for each sample as well as create the table neeeded for sleuth
os.system("python3 ./scripts/step3.py")

#Run script to get the find differentially expressed genes between the two timepoints/conditions
os.system("Rscript ./scripts/sleuthscript.R")

#Write required information from fdr_results into the log file
#Read the tab-delimited text file
file_path = "./PipelineProject_Jerrin_John/fdr_results.txt"
with open(file_path, 'r') as file:
    fdr_content = file.readlines()
#Append the content to the existing log file
log_file_path = "PipelineProject_Jerrin_John/PipelineProject.log"
with open(log_file_path, 'a') as log_file:
    log_file.writelines(fdr_content)

#Make bowtie2 script active
os.system("chmod +x ./scripts/step5.sh")

#Run shell script to map the donor reads to HCMV genome using bowtie2
os.system("./scripts/step5.sh")

#Make SPAdes script active
os.system("chmod +x ./scripts/step6.sh")

#Run shell script to generate assemblies for each donor using SPAdes
os.system("./scripts/step6.sh")

#Make a directory to store query fasta files
os.system('mkdir PipelineProject_Jerrin_John/queries')

#Script to find the longest Contig for the assembly of each donor and output as a FASTA file
os.system("python3 ./scripts/find_long_contig.py")

#Script to run a blast search with the two assemblies on Betaherpesvirinae subfamily
os.system("chmod +x ./scripts/ncbi_search.sh")
os.system("./scripts/ncbi_search.sh")

#Write required information from blast results into the log file


#Read the tab-delimited text file of Donor 1 blast results
file_path = "PipelineProject_Jerrin_John/donor1_blast_results.txt"
with open(file_path, 'r') as file:
    donor1_blast = file.readlines()

#Append the Donor1 blast content to the existing log file
log_file_path = "PipelineProject_Jerrin_John/PipelineProject.log"
with open(log_file_path, 'a') as log_file:
    log_file.write("Donor1:\n")
    log_file.write("sacc\tpident\tlength\tqstart\tqend\tsstart\tsend\tbitscore\tevalue\tstitle\n")
    log_file.writelines(donor1_blast)



#Read the tab-delimited text file of Donor 3 blast results
file_path = "PipelineProject_Jerrin_John/donor3_blast_results.txt"
with open(file_path, 'r') as file:
    donor3_blast = file.readlines()


#Append the Donor3 blast content to the existing log file
with open(log_file_path, 'a') as log_file:
    log_file.write("Donor3:\n")
    log_file.write("sacc\tpident\tlength\tqstart\tqend\tsstart\tsend\tbitscore\tevalue\tstitle\n")
    log_file.writelines(donor3_blast)

