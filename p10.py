import numpy as np
var=np.array([8,9,10,1,2,3,4,5,6,5])
res=np.where( var == 5 )
res1=np.sort(var)
res3=np.searchsorted(var,[10,9],side='left')
res2=np.unique(var)
print(res3)

np.random.shuffle(var)
print(var)