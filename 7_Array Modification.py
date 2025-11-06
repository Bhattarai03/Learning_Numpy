# Inserting the element in the array.
import numpy as np

array1=np.array([1,2,3,4,5,6,7,8,9])
array3=np.array([[20,21,22,23,24],[26,27,28,29,30]])

array6=np.array([20,21,22,23,24,25])
print(array1)

array2=np.insert(array1,4,77)
print(array2)

array4=np.insert(array3,2,[34,35],None)
print(array4)

arra=np.append(array1,[11,12,13,14,15])
print(arra)

# Concatenate two or more arrays
arr=np.concatenate((array1,array6))
print(arr)

# Removing the element in the array
arr1=np.delete(array1,4)
print(arr1)
new_array3=np.delete(array3,1,axis=0)
print(new_array3)

# Stacking two or more array horizontally and vertically
a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.vstack((a,b)))
print(np.hstack((a,b)))

# Splitting the elements from array
'''
Divide array in equal parts
np.hsplit() for horizontal split
np.vsplit() for vertical split

'''
ar=np.array([1,2,3,4,5,6,7,8])
ar2=np.array([[1,2,3],[4,5,6],[7,8,9]])
newar=np.split(ar,2)
newar1=np.hsplit(ar,4)
newar2=np.vsplit(ar2,3)
print(newar)
print(newar1)
print(newar2)