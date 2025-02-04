import numpy as np
arr=np.array([1,2,3])
arr1=np.array([10,20,30])
# print(np.concatenate([arr,arr1]))
# print(np.vstack([arr,arr1]))
# print(np.hstack([arr,arr1]))
print(np.array_split(arr,2))

