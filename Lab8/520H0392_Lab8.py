
import numpy as np
import matplotlib as plt

# Exericse 1: find the least square solution to Ax=b. For this case, the equation A^T*Ax = A^T * b with: A([[1,3],[2,4],[1,6]]) b=([[1],[4],[3]])
print('-------Exercise 1-------')

A = np.array([[1,3],[2,4],[1,6]])
b = np.array([[4,1,3]]).T

print('Least square solution:\n', np.linalg.lstsq(A,b,rcond=None)[0])

# Exercise 2

print('-------Exercise 2-------')

A = np.array([[0,0,1],[0,1,1],[1,2,1],[1,0,1],[4,1,1],[4,2,1]])
b = np.array([[0.5,1.6,2.8,0.8,5.1,5.9]]).T

print('Least square solution:\n', np.linalg.lstsq(A,b,rcond=None)[0])

# Exercise 3




