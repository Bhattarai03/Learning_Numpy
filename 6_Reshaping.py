'''
reshape (rows,column) specify new  shape
if dimension match '''
import numpy as np
array1=np.array([[1,2,3,4,5,6,7,8]])
print(array1)
reshape_=array1.reshape(2,4)   # For reshaping the dimension to multidimensional array..
print(reshape_)

# .ravel() -> view : it affect the original copy
# Flattem()-> it does not affect the original copy
array2=np.array([[1,2,3],[3,4,5],[6,7,8]])
print(array2)
r = array2.ravel()
f = array2.flatten()

r[0] = 100
print(array2)   # Will change, because r shares memory
f[0] = 999
print(array2)   # Won’t change, because f is a copy



