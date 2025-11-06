import numpy as np
array1=np.array([1,2,3,4,5,6,7,8,9,10])
print(array1[0])
print(array1[-1])



# Fancy inderxing = Selecting multiple element  at once
print(array1[[0,4,5,8]])

# Boolean masking : Condtion
print(array1[(array1 >3) & (array1<8)])
