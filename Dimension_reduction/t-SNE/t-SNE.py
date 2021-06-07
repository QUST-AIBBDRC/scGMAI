from sklearn.manifold import TSNE
#tsne降维
X_reduction = TSNE().fit_transform(X_test_reconstruct)
