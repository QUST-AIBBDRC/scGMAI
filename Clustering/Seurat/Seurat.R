library(Seurat)
library(dplyr)
library(Matrix)

data <- read.csv("data.csv", row.names = 1)
dense.size <- object.size(x = as.matrix(x = data))
sparse.size <- object.size(x = data)
mincell=0 
mingene=0 
pbmc <- CreateSeuratObject(counts = data)
pbmc <- NormalizeData(object = pbmc, normalization.method = "LogNormalize", scale.factor = 100)
pbmc <- FindVariableFeatures(object = pbmc)
pbmc <- ScaleData(object = pbmc)
pbmc <- RunPCA(object = pbmc)
pbmc <- FindNeighbors(object = pbmc)
pbmc <- FindClusters(object = pbmc)
write.csv(Idents(pbmc), file='data_Seurat.csv');
