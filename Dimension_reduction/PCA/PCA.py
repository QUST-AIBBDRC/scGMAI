from sklearn.decomposition import PCA
#PCA
pca = PCA(n_components=2)               
X_reduction = pca.fit_transform(X_test_reconstruct)           