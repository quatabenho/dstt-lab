import numpy as np
import sympy as sp
import matplotlib.pyplot as plt 



# 520H0392 - Truong Phuc Nguyen

# Ecercise 1
print('Exercise 1')

# Exercise 1a
x,y,z = sp.symbols('x, y, z')

eq1= sp.Eq(x+2*y+z,0)
eq2= sp.Eq(2*x-y+z,0)
eq3= sp.Eq(2*x+y,0)

print('Exercise 1a:',sp.solve((eq1,eq2,eq3),(x,y,z)))


# Exercise 1b 
x,y,z,t = sp.symbols('x,y,z,t')

eq1 = sp.Eq(2*x+y+z+t,1)
eq2 = sp.Eq(x+2*y+z+t,1)
eq3 = sp.Eq(x+y+2*z+2*t,1)
eq4 = sp.Eq(x+y+z+2*t,1)

print('Exercise 1b:',sp.solve((eq1,eq2,eq3,eq4),(x,y,z,t)))

# Exercise 2
print('\nExercise 2: Plot 2D Equation')


def plot2DEquation(x_arr, a, b, c):
    if b != 0:
        f_x = lambda x: (c - a*x)/b
        y_arr = list(map(f_x, x_arr))
        plt.plot(x_arr, y_arr, label = str(a)+'*x + '+ str(b)+'*y = '+str(c))
    elif a!=0:
            x_arr_new = np.full(len(x_arr), c/a)
            y_arr = np.linspace(-10, 10, num=len(x_arr))
            plt.plot(x_arr_new, y_arr, label = str(a)+'*x = '+str(c))
    else:
        print('Can not plot the equation')

x_arr = np.arange(-10, 11, 0.5)

# System 1
plot2DEquation(x_arr,1,1,0)
plot2DEquation(x_arr,1,-1,2)

x,y=sp.symbols('x,y')

eq1 = sp.Eq(x+y,0)
eq2 = sp.Eq(x-y,2)

sol=sp.solve((eq1,eq2),(x,y))
x=sol[x]
y=sol[y]

plt.title('System 1 - One Solution')
plt.scatter(x,y,color='r')
plt.legend()
plt.show()

# System 2
plot2DEquation(x_arr,1,1,5)
plot2DEquation(x_arr,2,2,12)

plt.title('System 2 - No Solution')
plt.legend()
plt.show()


# System 3
plot2DEquation(x_arr,1,1,5)
plot2DEquation(x_arr,3,3,15)

plt.title('System 3 - Infinite Solution')
plt.legend()
plt.show()


# System 4
plot2DEquation(x_arr,1,0,0)
plot2DEquation(x_arr,1,-1,2)

A = np.array([[1, 0], [1, -1]])
b = np.transpose([0,2])
X = np.linalg.solve(A, b)

x=X[0]
y=X[1]

plt.title('System 4 - One Solution')
plt.scatter(x,y,color='r')
plt.legend()
plt.show()


# Exercise 3
print('\nExercise 3: Plot 3D Equation')


def plotEquation3D(ax, x_arr, a, b, c, d, color):
    if c!=0:
        z_func = lambda x, y: (d - a*x - b*y) / c
        y_arr = x_arr.copy()
        X, Y = np.meshgrid(x_arr, y_arr)   
        Z = z_func(X, Y)
        ax.plot_surface(X, Y, Z, cmap = color, linewidth = 0, alpha = 0.5)
    else:
         if b!=0:
            y_arr = np.full(len(x_arr), d/b)
            X, Z = np.meshgrid(x_arr, x_arr)
            Y = np.full(X.shape, d/b)
            ax.plot_surface(X, Y, Z, cmap = color, linewidth = 0, alpha = 0.5)
         else:
            if a!=0:
                x_arr_new = np.full(len(x_arr), d/a)
                Y, Z = np.meshgrid(x_arr, x_arr)
                X = np.full(Y.shape, d/a)
                ax.plot_surface(X, Y, Z, cmap = color, linewidth = 0, alpha = 0.5)
            else:
                print('Can not plot the equation')

x_arr = np.arange(-5, 5, 0.1)

# System 1
fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')

plotEquation3D(ax, x_arr,25, 5, 1, 106.8, "Reds")
plotEquation3D(ax, x_arr, 64, 8, 1, 177.2, "Blues")
plotEquation3D(ax, x_arr, 144, 12, 2, 279.2, 'Greens')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('System 1')
plt.show()

# System 2
fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')

plotEquation3D(ax, x_arr, 1, 1, 1, 10, "Reds")
plotEquation3D(ax, x_arr, 1, 1, 1, 20, "Blues")
plotEquation3D(ax, x_arr, 3, 3, 3, 40, 'Greens')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('System 2')
plt.show()

# System 3
fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')

plotEquation3D(ax, x_arr, 1, 2, 1, 0, "Reds")
plotEquation3D(ax, x_arr, 2, -1, 1, 0, "Blues")
plotEquation3D(ax, x_arr, 2, 1, 0, 0, 'Greens')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('System 3')
plt.show()