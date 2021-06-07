from sklearn.decomposition import FastICA
#FastICA
transformer = FastICA(n_components=2,whiten=True)     
X_reduction = transformer.fit_transform(X_test_reconstruct)