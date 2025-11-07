
import random
import numpy as np
prices=np.random.randint(100, 10000, size=100)
discount= 10

final_price=prices - (prices * discount /100)
print(final_price)


# Adding element from two or more array of same dimension
ar1=np.array([1,2,3,4,5])
ar2=np.array([1,2,3,4,5])
result=ar1 + ar2
print(result)

# Adding element from two or more array of different shape
ar3=np.array([[1,2,3,4,5],[6,7,8,9,10]])
ar4=np.array([1,2,3,4,5])
print(ar3 + ar4)

# Adding uneven elment form two or more array
ar5=np.array([[1,2,3,4,5],[6,7,8,9,10]])
ar6=np.array([1,2])
ar7=ar6.reshape(2,1)

print(ar5 + ar7)