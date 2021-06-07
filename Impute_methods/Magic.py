import pandas as pd
import scanpy
import anndata

#Magic
data = pd.read_csv('data.csv') 
data=anndata.AnnData(data)
scanpy.external.pp.magic(data)