import numpy as np
arr1=np.array([1,2,3,4,5,6])
arr=np.array([[1,2,3,4,5,6],[1,2,3,4,5,6]])
arr3=np.array([[[1,2,3,4,5,6],[1,2,3,4,5,6],[1,2,3,4,5,6]]])

var=np.array([1,2,3,4])

vi=var.copy()
v1=var.view()
print(v1)
# print(arr)
# print(arr[0,1])
# print(arr.ndim)

# for i in arr:
#     for j in i:
#         print(j)

# for i in arr1:
#     print(i)
    
# for i in arr3:
#     for j in i:
#         for k in j:
#             print(k)
# print(arr3.ndim)

# for i in np.nditer(arr3):
#     print(i)

# for i in np.ndenumerate(arr3):
#     print(i)