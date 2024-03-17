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
