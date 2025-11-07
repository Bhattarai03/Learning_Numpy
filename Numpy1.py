import numpy as np
# 1 dimensional array
array=np.array([1,2,3,4,5,6,7,8,9,10])
print(array)
import numpy as np
# 2 dimensional array also known as matrix
arr2=np.array([[1,2,3],
               [1,4,5],
              [4,5,7]])
print(arr2)
# multidimensional array
arr3=np.array([[1,2,3],
               [1,4,5],
              [4,5,7]])
print(arr3)

# Creating array form python lists.
l=[1,2,3,4,5,6,7,8,9,0,]
arr4=np.array(l)
print(arr4)

# With default value of "0"
zeroarray=np.zeros(3)
print(zeroarray)

# one(shape)
onearray=np.ones((3,4))
print(onearray)

# With default value of any number
defvalue=np.full((2,3),5)
print(defvalue)

# Creating squence of number using array

arra=np.arange(0,100,2)
print(arra)

# Creating identity matrix
idenmatrix=np.eye((4))
print(idenmatrix)
