#load package
library(sleuth)

#read the table made from kallisto output
stab = read.table("./PipelineProject_Jerrin_John/sleuth_table.txt",header=TRUE)

#initialize sleuth object using sleuth_prep function from sleuth library
so = sleuth_prep(stab)

#fit a model comparing the two conditions (2dpi and 6dpi)
so = sleuth_fit(so, ~condition, 'full')

#fit the reduced model to compare in the likelihood ratio test without condition effect
so = sleuth_fit(so, ~1, 'reduced')

#perform the likelihood ratio test for differential expression between conditions 
so = sleuth_lrt(so, 'reduced', 'full')

#load the dplyr package for data.frame filtering
library(dplyr)

#extract the test results from the sleuth object 
sleuth_table = sleuth_results(so, 'reduced:full', 'lrt', show_all = FALSE) 

#filter most significant results (FDR/qval < 0.05) and sort by pval
sleuth_significant = dplyr::filter(sleuth_table, qval <= 0.05) |> dplyr::arrange(pval) 

#Get the wanted values in a new table
slim_sleuth <- sleuth_significant %>% select(target_id, test_stat, pval, qval)

#write FDR < 0.05 transcripts to file
write.table(slim_sleuth, file="./PipelineProject_Jerrin_John/fdr_results.txt",quote = FALSE,row.names = FALSE)


