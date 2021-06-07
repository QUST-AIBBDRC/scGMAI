##scGMAI

scGMAI: a Gaussian mixture model for clustering single-cell RNA-seq data based on deep autoencoder.

###scGMAI uses the following dependencies:
* python = 3.6 
* numpy = 1.16.3
* scipy = 1.4.1
* pandas = 0.25.3
* scikit-learn  = 0.22.1
* tensorflow = 1.13.1
* matplotlib = 3.0.3
* R = 3.6


###Guiding principles:

**We only provide one single-cell RNA-seq dataset, other datasets can be obtained from corresponding website.

**autoencoder_model:
   Autoencoder.py and AutoencoderRunner.py are the implementation of Autoencoder networks.
   
**Clustering:
1) CellTree:
   CellTree.m and CellTree.R are the implementation of CellTree.
2) GaussianMixture clustering:
   GaussianMixture clustering.py is the implementation of GaussianMixture clustering.
3) Kmeans:
   Kmeans.py is the implementation of Kmeans.
4) Seurat:
   Seurat.R is the implementation of Seurat.
5) SIMLR:
   SIMLR.R is the implementation of SIMLR.  
6) SNN-Cliq:
   SNN.m and cliq.py are the implementation of SNN-Cliq.
7) SpectralClustering:
   SpectralClustering.py is the implementation of SpectralClustering.
   
**Dimension_reduction:
1) FastICA:
   FastICA is the implementation of FastICA.
2) PCA:
   PCA is the implementation of PCA. 
3) t-SNE:
   t-SNE is the implementation of t-SNE.
4) UMAP:
   UMAP is the implementation of UMAP. 
5) ZIFA:
   ZIFA is the implementation of ZIFA.
6) SHARP:
   SHARP is the implementation of SHARP.
7) NMF:
   NMF is the implementation of NMF.
   
** Evaluation index:
   Evaluation index.py is the implementation of NMI,ARI,homogeneity and completeness.

** heatplot:
   heatplot.R is the implementation of heatplot.
   
** Impute methods:
1) DCA:
   DCA.py is the implementation of DCA.
2) Magic:
   Magic.py is the implementation of Magic. 
3) SAVER:
   SAVER.R is the implementation of SAVER.
4) scImpute:
   scImpute.R is the implementation of scImpute.
5) CIDR:
   CIDR.R is the implementation of CIDR.

** Preprocessing:
   Preprocessing.py is the implementation of DataPreprocessing.
   
You can download the datasets from the corresponding website. After that, you should prepare the data used in the Preprocessing code according to the steps below. 
Firstly, imputation data are obtained by autoencoder. Secondly, the imputation data is processed by FastICA. Finally, GaussianMixture clustering model cluster the cells from scRNA-seq data.

Input: data.csv

Output: pred_labels.csv and results.csv

The result.csv contains four evaluation indexes: NMI,ARI,Homogeneity and Completeness.



