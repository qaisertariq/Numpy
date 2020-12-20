#Q1
import numpy as np

#Q2
nulVec=np.zeros(10)

#Q3
vec=np.arange(10,50)

#Q4
np.shape(vec)

#Q5
print(vec.dtype)

#Q6
print(np.__version__)
print(np.show_config())

#Q7
print(vec.ndim)

#Q8
boolarr=np.full(10, True, dtype=bool)

#Q9
twdarr=np.random.randn(4,4)

#Q10
thdarr=np.random.randn(3,3,3)

#Q11
arr=np.arange(10)
arr=np.flip(arr)

#Q12
vec=np.zeros(10)
vec[4]=1

#Q13
iden=np.ones((3,3))

#Q14
arr=arr.astype(float)

#Q15
arr=arr1*arr2

#Q16
arr=arr1==arr2

#Q17
a[(a % 2 != 0)&(a<10)]

#Q18
a[(a % 2 != 0)&(a<10)]=-1

#Q19
arr[5:9]=12

#Q20
arr=np.ones((5,5))
arr[1:-1,1:-1] = 0

#Q21
arr2d[1][1]=12

#Q22
arr3d[0][0]=64    #just first one [[],] 
arr3d[0]=64       #first 2 [[],[]]

#Q23
arr=np.arange(10).reshape(2,5)
arr[0]

#Q24
arr=np.arange(10).reshape(2,5)
arr[1][1]

#Q25
print(arr[0:2,2])


#Q26
arr=np.random.randn(10,10)
np.min(arr)
np.max(arr)

#Q27
np.intersect1d(a,b)

#Q28
np.where(a==b)

#Q29
data[np.where(names!='Will')]

#Q30
data[np.where((names!='Will')&(names!='Joe'))]

#Q31
arr=np.arange(1,16).reshape(5,3)

#Q32
arr=np.arange(1,17).reshape(2,2,4)

#Q33
arr.reshape(2,4,2)

#Q34
arr=np.arange(0.2,10)
np.sqrt(arr)
arr[np.where(arr<0.5)]=0

#Q35
arr1=np.random.randn(12)
arr2=np.random.randn(12)
arr=np.fmax(arr1,arr2)

#36
np.sort(np.unique(names))

#Q37
np.setdiff1d(a, b)

#Q38
sampleArray[:,1]=newColumn

#Q39
np.dot(x,y)

#Q40
arr=np.random.randn(20)
np.cumsum(arr)




