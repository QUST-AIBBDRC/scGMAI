library(SIMLR)
data  <- read.csv("data.csv", row.names = 1);
a  <- SIMLR(data,n)
write.csv(a[["y"]][["cluster"]],file='data_SIMLR.csv')


