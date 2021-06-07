from sklearn.metrics.cluster import normalized_mutual_info_score
NMI = normalized_mutual_info_score(true_label,pred_label)
print(NMI)
from sklearn.metrics.cluster import adjusted_rand_score
ARI = adjusted_rand_score(true_label,pred_label)
print(ARI)
from sklearn.metrics.cluster import homogeneity_score
HOMO = homogeneity_score(true_label,pred_label)
print(homogeneity)
from sklearn.metrics.cluster import completeness_score
COMP = completeness_score(true_label,pred_label)
print(completeness)