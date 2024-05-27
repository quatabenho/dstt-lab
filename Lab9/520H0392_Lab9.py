# 520H0392 - Lab 9
import numpy as np
import matplotlib.pyplot as plt

# Exercise 6

print('-------Exercise 6-------')
times = np.array([1,2,3,4,5,6])
grams = np.array([2.1,3.5,4.2,3.1,4.4,6.8])
# y = a0 + a1*x + a2*x^2 + a3*x^3 
def cubic(x, a0, a1, a2, a3):
    return a0 * x**3 + a1 * x**2 + a2 * x + a3

xvals = np.linspace(0,7,100)
params = np.polyfit(times, grams, 3)
a0, a1, a2, a3 = params
yvals = cubic(xvals, a0, a1, a2, a3)

plt.scatter(times, grams)
plt.title('Ex 6: Cubic Model Fitting')
plt.plot(xvals, yvals, 'r-')
plt.legend()
plt.show()



# Exercise 7
print('\n-------Exercise 7-------')
print('Ex 7a: Scale 200%')
print('Ex 7b: Scale 50%')
print('Ex 7c: Symetric to the x-axis')
print('Ex 7d: Symetric to the y-axis')


# Exercise 8
print('\n-------Exercise 8-------')

print("Rotation matrix Rπ: Performs a 180-degree rotation counterclockwise.")
print("\nRotation matrix Rπ/3: Performs a 60-degree rotation counterclockwise.")


# Exercise 9
print('\n-------Exercise 9-------')
house = np.array([[-1, -1, -1.5, -1, 0.5, 0.5, 0.725, 0.725, 1,1.5,1,1,0,0,-0.5,-0.5,-1],
                  [0,1,1,2,2,2.5,2.5,2,2,1,1,0,0,0.8,0.8,0,0]])


# Exercise 9a
transMatrix = np.array([[2],[4]])
transHouse = house + transMatrix
plt.plot(house[0], house[1], 'ro-')
plt.plot(transHouse[0], transHouse[1], 'bo-')
plt.title('Ex 9a')
plt.grid()
plt.show()


# Exercise 9b
a = np.pi/3
rotMatrix = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
rotHouse = np.dot(rotMatrix, house)
plt.plot(house[0], house[1], 'ro-')
plt.plot(rotHouse[0], rotHouse[1], 'bo-')
plt.title('Ex 9b')
plt.grid()
plt.show()


# Exercise 9c
scaleMatrix = np.array([[2,0],[0,3]])
scaleHouse = np.dot(scaleMatrix, house)
plt.plot(house[0], house[1], 'ro-')
plt.plot(scaleHouse[0], scaleHouse[1], 'bo-')
plt.title('Ex 9c')
plt.grid()
plt.show()


# Exercise 9d
Shearx = 0.5
Sheary = -1.5

xshearMatrix = np.array([[1, Shearx], [0, 1]])
yshearMatrix = np.array([[1, 0], [Sheary, 1]])
xyshearMatrix = np.array([[1, Shearx], [Sheary, 1]])    

xshearHouse = np.dot(xshearMatrix, house)
yshearHouse = np.dot(yshearMatrix, house)
xyshearHouse = np.dot(xyshearMatrix, house)

plt.plot(house[0], house[1], 'ro-')
plt.plot(xshearHouse[0], xshearHouse[1], 'bo-')
plt.title('Ex 9d: Shear x')
plt.grid()
plt.show()

plt.plot(house[0], house[1], 'ro-')
plt.plot(yshearHouse[0], yshearHouse[1], 'bo-')
plt.title('Ex 9d: Shear y')
plt.grid()
plt.show()



plt.plot(house[0], house[1], 'ro-')
plt.plot(xyshearHouse[0], xyshearHouse[1], 'bo-')
plt.title('Ex 9d: Shear x and y')
plt.grid()
plt.show()
    

# Exercise 10
print('-------Exercise 10-------')
triangle = np.array([[1,3,1,1],[1,1,3,1]])
A = np.eye(2)

trans = np.dot(-A, triangle)
plt.plot(triangle[0], triangle[1], 'ro-')
plt.plot(trans[0], trans[1], 'bo-')
plt.title('Ex 10')
plt.grid()
plt.show()

# Exercise 11
print('-------Exercise 11-------')
F = np.array([[3,3,0,0,1,1,2.5,2.5,1,1,3],[4,5,5,0,0,1.8,1.8,2.8,2.8,4,4]])
T1 = np.array([-1,0,0,0,-1,0,0,0,1]).reshape(3,3)
T2 = np.array([1/4,0,0,0,1/4,0,0,0,1]).reshape(3,3)
T3 = np.array([1,0,5/4,0,1,-5/4,0,0,1]).reshape(3,3)
T4 = np.array([1/4,0,5/4,0,1/4,-5/4,0,0,1]).reshape(3,3)
T5 = np.array([-1/4,0,0,0,-1/4,0,0,0,1]).reshape(3,3)
T6 = np.array([-1/4,0,-5/4,0,-1/4,5/4,0,0,1]).reshape(3,3)
T7 = np.array([1,-1,5/4,0,0,5/4,0,0,1]).reshape(3,3)

Tb = np.array([1,0,-2,0,-2,1,9,0,1]).reshape(3,3)

# Exercise 11a
F = np.vstack((F, np.ones(F.shape[1])))
trans = np.dot(T1, F)
plt.plot(F[0], F[1], 'ro-')
plt.plot(trans[0],trans[1], 'bo-')
plt.title('Trans F with T1')
plt.grid()
plt.show()

trans = np.dot(T2, F)
plt.plot(F[0], F[1], 'ro-')
plt.plot(trans[0], trans[1], 'bo-')
plt.title('Trans F with T2')
plt.grid()
plt.show()


trans = np.matmul(T3,F)
plt.plot(F[0],F[1],'ro-')
plt.plot(trans[0],trans[1],'bo-')
plt.title("Trans F with T3")
plt.grid()
plt.show()

trans = np.matmul(T4,F)
plt.plot(F[0],F[1],'ro-')
plt.plot(trans[0],trans[1],'bo-')
plt.title("Trans F with T4")
plt.grid()
plt.show()

trans = np.matmul(T5,F)
plt.plot(F[0],F[1],'ro-')
plt.plot(trans[0],trans[1],'bo-')
plt.title("Trans F with T5")
plt.grid()
plt.show()

trans = np.matmul(T6,F)
plt.plot(F[0],F[1],'ro-')
plt.plot(trans[0],trans[1],'bo-')
plt.title("Trans F with T6")
plt.grid()
plt.show()

trans = np.matmul(T7,F)
plt.plot(F[0],F[1],'ro-')
plt.plot(trans[0],trans[1],'bo-')
plt.title("Trans F with T7")
plt.grid()
plt.show()

















    