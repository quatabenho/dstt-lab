import numpy as np 
import sympy as sp
import mathplotlib.pyplot as plt 

A = np.array([[1, 1], [1, -1]])

b = np.transpose([0,2])
X = np.linalg.solve(A, b)

print('vdl: X = ', X)

X = np.matmul(b, np.linalg.inv(A))
print('vd1 [by inverse matrix] X = ', X)
A = np.array([[1, 2, 1],[2, -1, 1], [2, 1, 0]])

b = np.transpose([0,0,0])
x = np.linalg.solve(A,b)
print('ex 1a : ', x)
# cah 3
x, y = sp.symbols('x,y')

#def eq
eq1 = sp.Eq((x+y),0)
eq2 = sp.Eq((x-y),2)

print('sympy x= ', sp.solve((eq1, eq2), (x,y)))

def plotEquation(x_arr, a, b, c):
    f_y = lambda x: (c - a*x)/b
    y_arr = list(map(f_y, x_arr))
    plt.plot(x_arr, y_arr, label = str(a)+'*x'+ str(b)+'*y ='+str(c))
    
x_arr = np.arange(-10, 11, 0.5)
plotEquation(x_arr,1,1,0)
plotEquation(x_arr,1,-1,2)

plt.title('vd 1')
plt.legend()
plt.show()

# graph eq 3D
def plotEquation3D(ax, x_arr, a, b, c, color):
    z_func = lambda x, y: (d - a*x - b*y) / c
    y_arr = x_arr.copy()
    X, Y = np.meshgrid(x_arr, y_arr)   
    Z = z_func(X, Y)
    ax.plot_surface(X, Y, Z, cmap = color, linewidth = 0, alpha = 0.5)
    
x_arr = np.arange(-5, 5, 0.1)
fig = plt.figure()
ax = fig.add_subplot(111,projection ='3D')

plotEquation3D(ax, x_arr, 1, 2, 1, 0, "Blues")
plotEquation3D(ax, x_arr, 2, -1, 1, 0, "Greens")
plotEquation3D(ax, x_arr, 2, 1, 1, 0, "Reds")