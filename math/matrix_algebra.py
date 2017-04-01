# Matrix Algebra

PLACE YOUR CODE HERE

import numpy as np

# Define matrices, vectors, and scalars.
A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])

u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])

a = 6

# Dimensions
A.shape
B.shape
C.shape
D.shape

u.shape
v.shape
w.shape


# Vector Operations
print(u + v)
print(u - v)
print(a*u)
print(np.dot(u, v))
print(np.linalg.norm(u))


# Matrix Operations
print(A + C) # matrices incompatible
print(A + np.transpose(C))
print(np.transpose(C) + 3*D)
print(B*A)
print(B*np.transpose(A)) # matrices incompatible

