import pandas as pd
import scanpy
import anndata

#DCA
data = pd.read_csv('data.csv') 
data=anndata.AnnData(data)
scanpy.external.pp.dca(data,copy=True)
