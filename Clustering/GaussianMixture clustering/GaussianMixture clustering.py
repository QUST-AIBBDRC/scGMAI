from sklearn import mixture
#GaussianMixture clustering
lowest_bic = np.infty
bic = []
n_components_range = range(1, 100)
for n_components in n_components_range:
    # Fit a Gaussian mixture with EM
    gmm = mixture.GaussianMixture(n_components=n_components)
    gmm.fit(X_reduction)
    bic.append(gmm.bic(X_reduction))
    if bic[-1] < lowest_bic:
       lowest_bic = bic[-1]
       best_gmm = gmm
bic = np.array(bic)
clustering = best_gmm
pred_label = clustering.predict(X_reduction)



