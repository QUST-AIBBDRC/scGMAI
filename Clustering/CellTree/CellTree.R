library(cellTree)

data <- read.csv("data.csv", row.names = 1)
lda.results = compute.lda(data)
p <- get.cell.dists(lda.results)
write.csv(p, sprintf("data_celltreeoutput.txt"))

