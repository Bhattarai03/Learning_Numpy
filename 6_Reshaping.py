'''
reshape (rows,column) specify new  shape
if dimension match '''
import numpy as np
array1=np.array([[1,2,3,4,5,6,7,8]])
print(array1)
reshape_=array1.reshape(2,4)
print(reshape_)

# .ravel() -> view : it affect the original copy
# Flattem()-> it does not affect the original copy
print(array1.ravel())
print(array1.flatten())
