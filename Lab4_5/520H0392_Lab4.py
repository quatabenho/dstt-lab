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
print('Exercise 2')


def plot2DEquation(x_arr, a, b, c):
    if b != 0:
        f_x = lambda x: (c - a*x)/b
        y_arr = list(map(f_x, x_arr))
        plt.plot(x_arr, y_arr, label = str(a)+'*x + '+ str(b)+'*y = '+str(c))
    else:
        if a!=0:
            x_arr_temp = np.full(len(x_arr), c/a)
            y_arr = np.linspace(-10, 10, num=len(x_arr))
            plt.plot(x_arr_temp, y_arr, label = str(a)+'*x = '+str(c))


x_arr = np.arange(-10, 11, 0.5)

# System 1
plot2DEquation(x_arr,1,1,0)
plot2DEquation(x_arr,1,-1,2)

x,y=sp.symbols('x,y')

eq1 = sp.Eq(x+y,0)
eq2 = sp.Eq(x-y,2)
plt.title('System 1')

sol=sp.solve((eq1,eq2),(x,y))
x=sol[x]
y=sol[y]

plt.scatter(x,y,color='g')
plt.legend()
plt.show()

# System 2
eq1 = sp.Eq(x+y,5)
eq2 = sp.Eq(3*x-5*y,15)
sol=sp.solve((eq1,eq2),(x,y))
x=sol[x]
y=sol[y]
    
plot2DEquation(x_arr,1,1,5)
plot2DEquation(x_arr,3,3,15)

plt.title('System 3')
plt.legend()
plt.show()


# plot2DEquation(x_arr,1,0,0)
# plot2DEquation(x_arr,1,-1,2)


# plt.title('3')
# plt.scatter(x,y, color = 'red')
# plt.legend()
# plt.show()

