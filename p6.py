import numpy as np
import statistics as stat
arr=np.array([1,2,3,5,6,7,5,9,6,1,3])
# print(np.mean(arr))
# print(np.median(arr))
# print(stat.mode(arr))
print(np.std(arr))
print(np.var(arr))
print(np.corrcoef(arr))
