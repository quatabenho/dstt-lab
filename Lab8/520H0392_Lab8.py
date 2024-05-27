
import numpy as np
import matplotlib.pyplot as plt

# Exericse 1: 
print('-------Exercise 1-------')

A = np.array([[1,3],[2,4],[1,6]])
b = np.array([[4,1,3]]).T

print('Least square solution:\n', np.linalg.lstsq(A,b,rcond=None)[0])

# Exercise 2

print('\n-------Exercise 2-------')

A = np.array([[0,0,1],[0,1,1],[1,2,1],[1,0,1],[4,1,1],[4,2,1]])
b = np.array([[0.5,1.6,2.8,0.8,5.1,5.9]]).T

print('Least square solution:\n', np.linalg.lstsq(A,b,rcond=None)[0])

# Exercise 3: 

# a) Exercise 3a: (0,1), (1,1), (2,2), (3,2)
A = np.array([[1,0],[1,1],[1,2],[1,3]])
b = np.array([[1,1,2,2]]).T

x = np.linalg.lstsq(A,b,rcond=None)

print('\nExercise 3a\nLeast square solution:\n', x[0])

plt.title('Exercise 3a')
plt.scatter([0,1,2,3],[1,1,2,2])
y = x[0][0] + x[0][1]*np.array([0,1,2,3])
plt.plot([0,1,2,3], y, 'r')
plt.show()

# Exercise 3b: (1,0), (2,1), (4,2), (5,3)

A = np.array([[1,1],[1,2],[1,4],[1,5]])
b = np.array([[0,1,2,3]]).T

x = np.linalg.lstsq(A,b,rcond=None)

print('\nExercise 3b\nLeast square solution:\n', x[0])

plt.title('Exercise 3b')
plt.scatter([1,2,4,5],[0,1,2,3])
y = x[0][0] + x[0][1]*np.array([1,2,4,5])
plt.plot([1,2,4,5], y, 'r')
plt.show()

# Exercise 3c: (-1,0), (0,1), (1,2), (2,4)

A = np.array([[1,-1],[1,0],[1,1],[1,2]])
b = np.array([[0,1,2,4]]).T

x = np.linalg.lstsq(A,b,rcond=None)

print('\nExercise 3c\nLeast square solution:\n', x[0])

plt.title('Exercise 3c')
plt.scatter([-1,0,1,2],[0,1,2,4])
y = x[0][0] + x[0][1]*np.array([-1,0,1,2])
plt.plot([-1,0,1,2], y, 'r')
plt.show()

# d) Exercise 3d: (2,3), (3,2), (5,1), (6,0)

A = np.array([[1,2],[1,3],[1,5],[1,6]])
b = np.array([[3,2,1,0]]).T

x = np.linalg.lstsq(A,b,rcond=None)
print('\nExercise 3d\nLeast square solution:\n', x[0])

plt.title('Exercise 3d')
plt.scatter([2,3,5,6],[3,2,1,0])
y = x[0][0] + x[0][1]*np.array([2,3,5,6])
plt.plot([2,3,5,6], y, 'r')
plt.show()



# Exercise 4
print('-------Exercise 4-------')
Mileage = np.array([2000,6000,20000,30000,40000])
friction = np.array([20,18,10,6,2])

value_x = np.linspace(min(Mileage),max(Mileage),100)

x = np.linalg.lstsq(np.array([Mileage,np.ones(len(Mileage))]).T,friction,rcond=None)[0]
y = x[1] + x[0]*value_x

print('Least square solution:\n', x)

plt.title('Exercise 4')
plt.scatter(Mileage,friction)
plt.plot(value_x,y,'r')
plt.show()


# Exercise 5:
print('\n-------Exercise 5-------')
x = np.array([1,2,3])
y = np.array([7.9,5.4,-9])

A = np.array([[np.cos(x[0]),np.sin(x[0])],[np.cos(x[1]),np.sin(x[1])],[np.cos(x[2]),np.sin(x[2])]])
b = np.array([y]).T

x = np.linalg.lstsq(A,b,rcond=None)

print('Least square solution:\n', x[0])

value_x = np.linspace(1,3,100)
y = x[0][0]*np.cos(value_x) + x[0][1]*np.sin(value_x)

plt.title('Exercise 5')
plt.scatter([1,2,3],[7.9,5.4,-9])
plt.plot(value_x,y,'r')
plt.show()





