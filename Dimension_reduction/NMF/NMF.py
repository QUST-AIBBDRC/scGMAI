import nimfa
#NMF
nmf = nimfa.Nmf(X_test_reconstruct, seed='random_vcol', rank=10, max_iter=100)
nmf_fit = nmf()
X_reduction=nmf_fit.fit.basis()