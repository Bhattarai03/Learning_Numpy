import numpy as np
ar1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
ar2=np.array([[1,2,3,4,5],[5,6,4,3,2]])
ar3=np.concatenate([ar1,ar2],axis=1)
print(ar3)