import numpy as np
#numpy library funcation is this
a = np.array([5,5,5,5,5])
print(a)
print(len(a))
print(type(a))
print(a[0])
print(a[0:])

b = np.zeros([5])
print(b)

c = np.ones([5])
print(c)

d = np.empty([5])
print(d) 

e = np.arange(6)
print(e)


f = np.arange(2,10)
print(f)

g = np.arange(2,20,2)
print(g)

e = np.linspace(2,10,num=5)
print(e)
print("*********************************")
print("*********************************")
print("*********************************")

#define 1D,2D,3D array in python
print("1D array")
A = np.ones(5,dtype=np.int8)
print(A)

B = np.ones(5,dtype=np.float64)
print(B)

print("2D array")
C =np.ones((3,4))
print(C)

D = np.zeros((4,5))
print(D)

E = np.empty((3,4))
print(E)

print("making a reshipe 3D array")
W=np.arange(24).reshape(2,3,4)
print(W)

print("*********************************")
print("*********************************")
print("*********************************")
# numpy array in ADDING and REMOVING and SORTING and ELEMENT
arr = np.array([1,9,8,4,7,6,5,3,2,0,10])
arr =np.sort(arr)
ar = np.array ([11,12,13,14,15,16,17,18,19,20])
ar= np.sort(ar)
print(np.concatenate((arr,ar)))
a = np.array([[1,2,3,4],[5,6,7,8]])
b = np.array([[9,10,11,12]])
print(np.concatenate((a,b),axis=0))
print("*********************************")
print("*********************************")
print("*********************************")
#array_example shape and size and array
array_example = np.array([[[1,2,3],
                          [4,5,6]],
                         [[7,8,9],
                          [10,11,12]],
                         [[13,14,15],
                          [16,17,18]]])
print(np.ndim(array_example))
print(np.size(array_example))
print(np.shape(array_example))

a = np.array([1,2,3,4,5,6,7,8,9])
print(a)
b = a.reshape(3,3)
print(b)

B = np.reshape(a, newshape=(1,9),order='F')
print(B)

print("*********************************")
print("*********************************")
print("*********************************")
#How to convert a 1D array into a 2D array (how to add a new axis to an array)
R = np.array([1,2,3,4,5,6])
print(R.shape)

D2 = R[np.newaxis,:]
print(D2.shape)

b = np.expand_dims(a,axis=0)
print(b)

a=np.expand_dims(a,axis=1)
print(a)

a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
z = a.sum(axis=0)
print(z)
z = a.sum(axis=1)
print(z)

print("*********************************")
print("*********************************")
print("*********************************")
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-5, 5, 0.20)
Y = np.arange(-5, 6, 0.20)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
plt.show()
