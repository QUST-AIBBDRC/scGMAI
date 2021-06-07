library(Seurat)
library(dplyr)
library(Matrix)
library(ComplexHeatmap)
library(circlize)
data <- read.csv("data.csv", row.names = 1);    
data <- CreateSeuratObject(counts = data)  
label <- read.csv("data_pred.csv",header=FALSE);
label <-t(label)
Idents(data) <- label 
pbmc.markers <- FindAllMarkers(data)  
top5 <- pbmc.markers %>% group_by(cluster) %>% top_n(n =5, wt = avg_logFC)
mat<-GetAssayData(data, slot = "counts")  
gene_features <- top5
cluster_info <- sort(data@active.ident)
mat <- as.matrix(mat[top5$gene, names(cluster_info)])
Heatmap(mat,
        width = unit(8, "cm"), 
        height = unit(6.5, "cm"),
        name = "Data", 
        border = TRUE,
        rect_gp = gpar(col = "gray55", lwd = 0.01),
        cluster_rows = FALSE,
        cluster_columns = TRUE,
        show_column_names = FALSE,
        show_row_names = TRUE,
        row_names_gp = gpar(family = 'Broman',fontsize = 7.5, fontface = "bold"),
        column_split = cluster_info,
        top_annotation = HeatmapAnnotation(
          Cluster = cluster_info, 
          annotation_legend_param =(cluster=list(anno_block(gp = gpar(fill = col),
                                                             labels = levels(cluster_info))
          ))), 
        column_title = 'Cell Type',
        column_title_gp = gpar(family = 'Broman', fontsize = 15),
        row_title = "Gene Makers",
        row_title_gp = gpar(family = 'Broman', fontsize = 15))



