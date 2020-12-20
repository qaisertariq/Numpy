import numpy as np

nulVec=np.zeros(10)

vec=np.arange(10,50)

np.shape(vec)

print(vec.dtype)

print(np.__version__)
print(np.show_config())

print(vec.ndim)

boolarr=np.full(10, True, dtype=bool)

twdarr=np.random.randn(4,4)

thdarr=np.random.randn(3,3,3)

arr=np.arange(10)
arr=np.flip(arr)

vec=np.zeros(10)
vec[4]=1
