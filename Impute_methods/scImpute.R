library(scImpute)
scimpute(
    count_path = "D:/Documents/R/data.csv", 
    infile = "csv",          
    outfile = "csv",          
    out_dir = "D:/Documents/R/data_scImpute.csv",
    labeled = FALSE,          
    drop_thre = 0.5,          
    Kcluster = n,           
    ncores = 1)      
