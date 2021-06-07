from sklearn.cluster import KMeans
#KMean clustering
clustering = KMeans(n_clusters=n).fit(X_reduction)
pred_label = clustering.predict(X_reduction)




