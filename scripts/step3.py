import os

# Directory containing the abundance.tsv files
results_dir = "kallisto_results"

# Function to calculate statistics
def calculate_tpm_stats(tpm_values):
    min_tpm = min(tpm_values) #Find minimum value in list of TPMs
    max_tpm = max(tpm_values) #Find max value in list of TPMS
    tpm_values.sort() #sort the TPMs from lowest to highest
    n = len(tpm_values) #store length of list
    if n % 2 != 0: #if the length is an odd number, the median tpm is the middle number in the list
        med_tpm = tpm_values[n // 2] 
    else: #if the length is an even number
        med_tpm = (tpm_values[n // 2 - 1] + tpm_values[n // 2]) / 2 #Find the average TPM between the two middle numbers
    mean_tpm = sum(tpm_values) / n #Calculate average
    return min_tpm, max_tpm, med_tpm, mean_tpm

final_result_list = [["sample", "condition", "min_tpm", "med_tpm", "mean_tpm", "max_tpm"]]
sleuth_list = [["sample", "condition", "path"]]
# Loop through each abundance.tsv file in the results directory
for root, dirs, files in os.walk(results_dir): #Loops through all directories in results directory
    for file in files:
        curr_sample_info = []
        if file == "abundance.tsv":
            abundance_file = os.path.join(root, file)
            # Initialize list to store TPM values
            tpm_values = []
            # Open the abundance.tsv file and read line by line
            with open(abundance_file, 'r') as f:
                # Skip the header 
                next(f)
                # Read each line and extract the TPM value (5th column)
                for line in f:
                    columns = line.strip().split('\t') #Split the columns
                    tpm = float(columns[4])  # Column 5 contains the TPM values
                    tpm_values.append(tpm) #Add tpm to list
                    # Calculate the statistics if there are TPM values
            min_tpm, max_tpm, median_tpm, mean_tpm = calculate_tpm_stats(tpm_values)
            sample_id = root[17:]
            curr_sample_info.append(str(sample_id))
            if sample_id == "SRR5660030" or sample_id == "SRR5660044": #add correct condition depending on sample id
                condition = "2dpi"
                curr_sample_info.append(condition)
            else:
                condition = "6dpi"
                curr_sample_info.append(condition)
            #Add remaining info to list
            curr_sample_info.append(str(min_tpm))
            curr_sample_info.append(str(median_tpm))
            curr_sample_info.append(str(mean_tpm))
            curr_sample_info.append(str(max_tpm))
            #Add current sample info to total list
            final_result_list.append(curr_sample_info)
            sleuth_list.append([sample_id,condition,root])
        
# Specify the log file path to write to 
log_file_path = "PipelineProject_Jerrin_John/PipelineProject.log"

# Open the log file in append mode
with open(log_file_path, 'a') as log_file:
    for row in final_result_list:
        # Join the list into a string with tab separation and write it to the file
        log_file.write("\t".join(map(str, row)) + "\n")
    log_file.write('\n')

#Creates sleuth table for next step
sleuth_table = "./PipelineProject_Jerrin_John/sleuth_table.txt"
with open(sleuth_table, 'w') as sleuth_info:
    for row in sleuth_list:
        # Join the list into a string with tab separation and write it to the file
        sleuth_info.write("\t".join(map(str, row)) + "\n")

