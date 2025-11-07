# np.isnan(array)  for detecting missing value
# np.nan_to_name()  for adding the value in missing space
# np.isinf for detecting infinite value
import numpy as np
arr= np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))

newaar=np.nan_to_num(arr,nan=3)
print(newaar)

arr2=np.array([1,2,3,np.inf,6,np.inf])
print(np.isinf(arr2))
newaar2=np.nan_to_num(arr2, posinf=1000 ,neginf=-1000 )
print(newaar2)