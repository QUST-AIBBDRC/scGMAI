import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
data = pd.read_csv('data.csv')
data = pd.DataFrame(data)                                                  
true_label = pd.read_csv('data_label.csv')
true_label=np.array(true_label)
true_label = true_label.ravel()   
pred_label = pd.read_csv('data_pred.csv')
pred_label=np.array(pred_label)
pred_label = pred_label.ravel()    
r1 = pd.Series(pred_label).value_counts()  
r2 = pd.Series(true_label).value_counts()
r = pd.concat([pd.Series(pred_label, index = data.index), data ], axis = 1)  
r.columns = [u'label'] + list(data.columns) 
tsne = TSNE()
tsne.fit_transform(data) 
a = pd.DataFrame(tsne.embedding_, index = data.index)
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False 
d = a[r[u'label'] == 0]
plt.scatter(d[0], d[1], c='r',marker='.',label="0")
d = a[r[u'label'] == 1]
plt.scatter(d[0], d[1], c='g',marker='.',label="1")
d = a[r[u'label'] == 2]
plt.scatter(d[0], d[1], c='y',marker='.',label="2")     
d = a[r[u'label'] == 3]
plt.scatter(d[0], d[1], c='b',marker='.',label="3")
plt.xlabel("tSNE1",fontsize = 20)
plt.ylabel("tSNE2",fontsize = 20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(bbox_to_anchor=(1.0, 0),loc=3, borderaxespad=0,fontsize=20)
plt.tight_layout()
plt.show()
