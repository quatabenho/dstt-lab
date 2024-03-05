
import numpy as np


# Exercise 1: Create vectors and get the number of elements
print('Exercise 1: Create vectors and get the number of elements')
x = np.array([1,3,5,2,9])
y = np.array([-1,3,15,27,29])

print('Vector x = ',x,'\nNumber of element in vector x: ',len(x))
print('Vector y = ',y,'\nNumber of element in vector y: ',len(y))

# Exercise 2: Create the following vectors with n elements
print('\nExercise 2: Create the following vectors with n elements')
n = 11
# Ex 2a
b = np.arange(12, 12+n*2,2)
print('b = ', b)

# Ex 2b
c = np.arange(31,n+49,2)
print('c = ',c)

# Ex 2c
x = np.arange(-5,6,1)
print('x = ',x)

# Ex 2d
y = np.arange(5,-6,-1)
print('y = ',y)

# Ex 2e
z = np.arange(10,-5,-2)
print('z = ',z)

# Ex 2f
w = 1 / 2**np.arange(n)
print('w = ',np.round(w,2))

# Ex 2g
d = [1, 1]
for i in range(2,8):
    d.append(d[i-1] + d[i-2])
d = [1.0/d[i] for i in range(len(d))]
print('d = ', np.round(d,2))

# Ex 2h
# Func check so nguyen to
def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

e = np.array([1 / i for i in range(2,n) if isPrime(i)])
print('e = ',np.round(e,2))

# Ex 2i
a = [1,3]

for i in range(2,n):
    a.append(a[i-1] + (i + 1))
a = np.array(a)
print('a = ',a)

# Ex 2j
ex2j = [1 / (i**2 + 1) for i in range(1, n + 1)]
print('n = ',np.round(ex2j, 2))

# Ex 2k
p = np.array([i / (i + 1) for i in range(n)])
print('p = ',np.round(p,2))

# Ex 2l
o = [chr(i) for i in range(97, 123)]
print('o = ',o)

# Ex 2m
s = [chr(i) for i in range(65, 91,3)]
print('s = ',s)


# Exercise 3: Create the following vector by logarithmic spacing method
print('\nExercise 3: Create the following vector by logarithmic spacing method')
x = np.logspace(1,n,n)
np.set_printoptions(formatter={'float': lambda x: f"10^{int(np.log10(x))}"}) 
print('x = ',x)


# Exercise 4: Create vector z = x + y
print('\nExercise 4: Create vector z = x + y')
x = [1,2,3]
y = [98,12,33]
print('z = ',x + y)


# Exercise 5: Create vector z
print('\nExercise 5: Create vector z')
x = [1,2,3]
y = [4,5,6]
print('z = ',np.array([x, y]))


# Exercise 6: Get elements from vector x
x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
print('\nExercise 6: Get elements from vector x =',x)

# Ex 6a
print('\nExercise 6a: First 6 elements:', x[0:6]) 

# Ex 6b
print('Exercise 6b: Last 5 elements ', x[-6:len(x)]) 

# Ex 6c
print('Exercise 6c: First, fourth and last elements:', x[[0, 3, -1]])

# Ex 6d
print('Exercise 6d: First, third, fifth and seven elements:', x[[0, 2, 4, 6, -1]])

# Ex 6e
print('Exercise 6e: Elements with odd indices:', x[1:len(x):2] )

# Ex 6f
print('Exercise 6f: Elements with even indices:', x[0:len(x):2] )


# Exercise 7: Calculate
x = np.array([3, 11, -9, -131, -1, 1, -11, 91, -6, 407, -12, -11, 12, 153, 371])
print('\nExercise 7: Calculate vector x =',x)

# Ex 7a
print('Exercise 7a: Maximize element:', np.max(x))

# Ex 7b
print('Exercise 7a: Minimize element:', np.min(x))

#  Ex 7c
print('Exercise 7c: Index of value > 10:', x[x > 10])

# Ex 7d
print('Exercise 7d: Reverse vector x:', x[::-1])

# Ex 7e
print('Exercise 7e: Sort vector x in ascending order:', np.sort(x))

# Ex 7f
print('Exercise 7f: Sort vector x in descending order:', np.sort(x)[::-1])

# Ex 7g
print('Exercise 7g: Count how many times have that xi + xj = 0, i != j:', sum([1 for i in range(len(x)) for j in range(i+1, len(x)) if x[i] + x[j] == 0]))

# Ex 7h
print('Exercise 7g: Count total number of duplicate elements:', len(x) - len(np.unique(x)))

# Ex 7i
print('Exercise 7i: Create a new vector y which y_i = x_i + x_n-i-1:', x + x[::-1])
# y = np.zeros(len(x))
# for i in range(len(x)): 
#     y[i] = x[i] + x[len(x)-i-1]
# print('y = ',y)

# Ex 7j
# check ams 
def isAmstrong(num):
    if num<0:
        return False
    num_str = str(num)
    n = len(num_str)
    return num == sum(int(digit) ** n for digit in num_str)
w = np.array([i for i in x if isAmstrong(i)])
print('Ex 7j: Create a new w vector which contains Armstrong/Narcissistic numbers in x, w =', w)

# Ex 7k
print('Ex 7k: Delete all negative elements in x:', x[x >= 0])

# Ex 7l
print('Ex 7l: Find median value of x:', np.median(x))

# Ex 7m
print('Ex 7m: Calculate sum of all values which are less than mean value in x:', sum(x[x < np.mean(x)]))

# Ex 7n
print('Ex 7n: Create new vector which each negative value is replaced by its absolute value:', np.abs(x))