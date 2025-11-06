# Shape helps to identify the rows and column in the multidiensional array.
import numpy as np
arr2=np.array([[1,2,3],
               [1,4,5],
              [4,5,7]])
print(arr2.shape)

# Size helps to find out the total no. of element in the arrays.
print(arr2.size)

# ndim = no. of dimensions
print(arr2.ndim)

# .dtype = data type in the array
print(arr2.dtype)

# astype = To change the data type in th array
d=arr2.astype(float)
print(d)
print(d.dtype)


