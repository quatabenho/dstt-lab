# 520H0392 - Truong Phuc Nguyen

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# 520H0392 - Truong Phuc Nguyen

# Exercise 6: Find the interpolating polynomial p(t)=a0+a1*t+a2*t^2 for the data (1,6),(2,15),(3,38).That is, find a0, a1 and a2
print('Exercise 6')
a0, a1, a2 = sp.symbols('a0 a1 a2')
eq1= sp.Eq(a0+a1*1+a2*1**2,6)
eq2= sp.Eq(a0+a1*2+a2*2**2,15)
eq3= sp.Eq(a0+a1*3+a2*3**2,38)
result = sp.solve((eq1,eq2,eq3),(a0,a1,a2))
print('a0 = ',result[a0],'\na1 = ',result[a1],'\na2 = ',result[a2])

# Exercise 7: A group took a trip on a bus, at $3 per child and $3.2 per adult for a total of $118.4. They took the train back at $3.5 per child and $3.6 per adult for a total of $135.2. How many children and how many adults?
print('\nExercise 7')
children, adult = sp.symbols('c a')
eq1= sp.Eq(3*children+3.2*adult,118.4)
eq2= sp.Eq(3.5*children+3.6*adult,135.2)
result = sp.solve((eq1,eq2),(children,adult))

print('Number of children = ',round(result[children]),'\nNumber of adults = ',round(result[adult]))



# Exercise 8

print('\nExercise 8')
x,y,z,t = sp.symbols('x y z t')
eq1= sp.Eq(2*x-4*y+4*z+0.077*t,3.86)
eq2= sp.Eq(-2*y+2*z-0.056*t,-3.47)
eq3= sp.Eq(2*x-2*y,0)
result = sp.solve((eq1,eq2,eq3),(x,y,z,t))

print('x = ',result[x],'\ny = ',result[y],'\nz = ',result[z])


# Exercise 9

print('\nExercise 9')
R,G,B = sp.symbols('R G B')
X,Y,Z = sp.symbols('X Y Z')
XYZ = np.array([9,32,150])
A = np.array([[0.61,0.29,0.15],[0.35,0.59,0.063],[0.04,0.12,0.787]])

A1 = np.linalg.inv(A)

RGB = np.dot(A1,XYZ)
print('R = ',RGB[0],'\nG = ',RGB[1],'\nB = ',RGB[2])


# Exercsie 10
print('\nExercise 10')
A = np.array([[0.25,0.15,0.1],[0.4,0.15,0.2],[0.15,0.2,0.2]])
d = np.array([[100,100,100]]).T

print('p = ',np.matmul((np.linalg.inv(np.eye(3)-A)),d))

# Exercise 11
print('\nExercise 11')
x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')

eq1 = sp.Eq((3*x1-x3),0)
eq2 = sp.Eq((8*x1-2*x4),0)
eq3 = sp.Eq((2*x2-2*x3-x4),0)
result = sp.solve((eq1,eq2,eq3),(x1,x2,x3,x4))

x4_value = 4
result = {var: sol.subs(x4, x4_value) for var, sol in result.items()}
result[x4] = x4_value

print('x1 = ',result[x1],'\nx2 = ',result[x2],'\nx3 = ',result[x3],'\nx4 = ',result[x4])

