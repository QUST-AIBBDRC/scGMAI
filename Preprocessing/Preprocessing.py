import numpy as np
import pandas as pd
data = pd.read_csv('data.csv',header=None) 
data = data.drop(labels=None,axis=0,index=0,inplace=False)
data1=np.array(data)
i=0
for i in range(data1.shape[1]):
    j=data1[:,i];
    sum0 = np.sum(j==0);
    if (sum0/data1.shape[0])>=0.95:
        data=data.drop(labels=None,axis=1,index=None,columns=i,inplace=False);
    else:
        data=data;
    i=i+1;    
print(data)

X_train = np.log2(data+1)
np.savetxt("X_train.csv",X_train,delimiter=',') 