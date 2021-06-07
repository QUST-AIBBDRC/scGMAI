from sklearn.cluster import SpectralClustering
#Spectral Clustering
clustering = SpectralClustering(n_clusters=n).fit(X_reduction)
pred_label = clustering.labels_




