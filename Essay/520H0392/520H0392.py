
import numpy as np
import sympy as sp


# Task 1:
print("Task 1")

A = np.random.randint(1, 100, (10, 10))
B = np.random.randint(1, 20, (2, 10))
C = np.random.randint(1, 20, (10, 2))

# This is the 3 output matrices that I use to print in my report -> select all and [Ctrl + K + U] to uncomment (if needed)

# A = np.array([[82, 42, 32, 47, 52, 68, 84, 84, 43, 68],
#               [74, 77, 34, 22, 1, 63, 25, 99, 34, 16],
#               [18, 13, 43, 84, 16, 41, 88, 57, 91, 73],
#               [99, 91, 3, 18, 84, 55, 32, 64, 96, 58],
#               [49, 81, 71, 34, 93, 48, 54, 19, 57, 50],
#               [96, 59, 13, 87, 34, 35, 63, 81, 75, 2],
#               [96, 95, 96, 9, 26, 5, 52, 82, 16, 33],
#               [52, 60, 72, 63, 45, 32, 41, 84, 37, 34],
#               [56, 17, 49, 67, 66, 26, 54, 19, 52, 70],
#               [40, 21, 21, 24, 86, 81, 54, 80, 73, 24]])

# B = np.array([[5, 5, 10, 1, 14, 8, 3, 15, 7, 11],
#               [2, 8, 16, 8, 16, 13, 17, 10, 7, 11]])

# C = np.array([[8, 9],
#               [14, 12],
#               [6, 3],
#               [3, 11],
#               [13, 8],
#               [7, 13],
#               [10, 18],
#               [1, 18],
#               [16, 15],
#               [11, 13]])

print('A = \n', A)
print('\nB = \n', B)
print('\nC = \n', C)


# Task 1a: Calculate A + A^T + C*B + (B^T)*(C^T)
print('\nTask 1a\n',  A + A.T + np.dot(C, B) + np.dot(B.T, C.T))


# Task 1b: calculate (A/10)^1 + (A/11)^2 + (A/12)^3 + ... + (A/19)^10
print('\nTask 1b\n', np.sum([(np.linalg.matrix_power(A/(i+10), i+1)) for i in range(10)], axis=0))


# Task 1c: Save odd rows of the matrix A into a new matrix, and print the resultant matrix to the screen.
task1c = A[::2] 
print('\nTask 1c = \n', task1c)


# Task 1d: Save odd integer numbers in the matrix A into a new vector, and print the resultant vector to the screen. 
task1d = A[A % 2 == 1]
print('\nTask 1d = \n', task1d)



# Task 1e: Save prime numbers in the matrix A into a new vector, and print the resultant vector to the screen. 
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


task1e = []
for i in range(10):
    for j in range(10):
        if isPrime(A[i][j]):
            task1e.append(A[i][j])
print('\nTask 1e = \n', np.array(task1e))


# Task 1f Given a matrix D = C*B, reverse elements in the odd rows of the matrix D, and print the resultant matrix to the screen.

D = np.dot(C, B)

task1f = D.copy()
task1f[::2] = task1f[::2, ::-1]

print('\nTask 1f = \n', task1f)


# Task 1g: Regarding the matrix A, find the rows which have maximum count of prime numbers, and print the rows to the screen
# A = np.array([[1,2,2,4],[5,7,7,8],[9,10,11,12],[13,2,3,4]]) 

def maxPrimeRow(A):
    temp = []
    maxCount = 0
    for i in range(A.shape[0]):
        count = 0
        for j in range(A.shape[1]):
            if isPrime(A[i][j]):
                count += 1
        if count > maxCount:
            maxCount = count
            temp = [list(A[i])]
        elif count == maxCount:
            temp.append(list(A[i]))
    return temp

print('\nTask 1g = \n', maxPrimeRow(A))


# Task 1h: Regarding the matrix A, find the rows which have longest sequence of odd numbers, and print the rows to the screen
# A = np.array([[1,2,3,5,8],[5,7,7,8,9],[0,2,4,6,8],[8,2,9,3,7]])

def longestOddSeq(A):
    temp = []
    countOdd = 0
    for i in range(A.shape[0]):
        count = 0
        for j in range(A.shape[1]):
            if A[i][j] % 2 == 1:
                count += 1
            else:
                count = 0
            if count > countOdd:
                countOdd = count
                temp = [list(A[i])]
            elif count == countOdd:
                temp.append(list(A[i]))
    return temp

print('\nTask 1h = \n', longestOddSeq(A))
