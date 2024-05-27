# 520H0392 - Lab 10
import numpy as np 
import matplotlib.pyplot as plt

# Exericise 1
print('-------Exercise 1-------')
A = np.array([[-1,3.5,14],[0,5,-26],[0,0,2]])
B = np.array([[-2,0,0],[99,0,0],[10,-4.5,10]])
C = np.array([[5,5,0,2],[0,2,-3,6],[0,0,3,-2],[0,0,0,5]])
D = np.array([[3,0,0,0],[6,2,0,0],[0,3,6,0],[2,3,3,-5]])
E = np.array([[3,0,0,0,0],[-5,1,0,0,0],[3,8,0,0,0],[0,-7,2,1,0],[-4,1,9,-2,3]])

def calED(A):
    print('Eigenvalues =', np.linalg.eigvals(A))
    print('Det = ',np.prod(np.linalg.eigvals(A)))

print('Exercise 1a')
calED(A)

print('\nExercise 1b')
calED(B)

print('\nExercise 1c')
calED(C)

print('\nExercise 1d')
calED(D)

print('\nExercise 1e')
calED(E)


# Exercise 2
print('-------Exercise 2-------')

A = np.array([[-6,28,21],[4,-15,-12],[8,32,25]])
a = [32, 31.9, 31.8, 32.1, 32.2]
t = np.linspace(0,3,100)
for i in a:
    A[2][2] = i
    p = np.poly(A)
    plt.plot(t, np.polyval(p, t), label = 'a = ' + str(i))
plt.legend()
plt.title('Exercise 2')
plt.show()


# Exercise 3
print('\n-------Exercise 3-------')
M = np.array([[-3,-5,-7],[-2,1,0],[1,5,5]])
eigenvalues, eigenvectors = np.linalg.eig(M)

print('Exercise 3a')
print('Eigenvalues =', eigenvalues)

print('\nExercise 3b')
print('Eigenvectors =', eigenvectors)

for i in range(len(eigenvalues)):
    print('For eigenvalue', eigenvalues[i], 'the eigenvector is', eigenvectors[:,i])

# Exercise 4
print('\n-------Exercise 4-------')
A = np.array([[ -2,2,-3],[2,1,-6],[-1,-2,0]])
AT = np.transpose(A)
A_inv = np.linalg.inv(A)

eigenvalues, eigenvectors = np.linalg.eig(A)
print('Exercise 4a')
print('Eigenvalues of A=', eigenvalues)
print('Eigenvectors of A=', eigenvectors)

print('\nExercise 4b')
eigenvalues, eigenvectors = np.linalg.eig(AT)
print('Eigenvalues of A^T=', eigenvalues)
print('Eigenvectors of A^T =', eigenvectors)

eigenvalues, eigenvectors = np.linalg.eig(A_inv)
print('\nEigenvalues of A^-1 =', eigenvalues)
print('Eigenvectors of A^-1 =', eigenvectors)


# Exercise 5
print('\n-------Exercise 5-------')

A1 = np.array([[4,-5],[2,-3]])
A2 = np.array([[0,2],[0,1]])
A3 = np.array([[2,3],[1,4]])
A4 = np.array([[1,2,-2],[-2,5,-2],[-6,6,-3]])
A5 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

def isDiagonalizable(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    D = np.diag(eigenvalues)
    P = eigenvectors
    if np.allclose(A, np.dot(np.dot(P,D),np.linalg.inv(P))):
        print('The given matrix is diagonalizable')
    else:
        print('The given matrix is not diagonalizable')

print('A1: ', end = '')
isDiagonalizable(A1)

print('\nA2: ', end = '')
isDiagonalizable(A2)

print('\nA3: ', end = '')
isDiagonalizable(A3)

print('\nA4: ', end = '')
isDiagonalizable(A4)

print('\nA5: ', end = '')
isDiagonalizable(A5)


# Exercise 6
print('\n-------Exercise 6-------')

A = np.array([[1,2,-2],[0,3,-2],[0,0,1]])

eigenvalues, eigenvectors = np.linalg.eig(A)
D = np.diag(eigenvalues)
P = eigenvectors
P_inv = np.linalg.inv(P)
print('Eigenvalues of A =', eigenvalues)
print('\nP^-1AP =', np.round(np.dot(np.dot(P_inv,A),P)))


# Exercise 7
print('\n-------Exercise 7-------')

A1 = np.array([[1,0],[0,-3]])
A2 = np.array([[-5,0],[0,0]])
A3 = np.array(([[np.sqrt(6),1],[0,np.sqrt(6)]]))
A4 = np.array([[np.sqrt(3),2],[0,np.sqrt(3)]])

print('Matrix A1:')
print('U = ', np.linalg.svd(A1)[0])
print('Sigma = ', np.linalg.svd(A1)[1])
print('VH = ', np.linalg.svd(A1)[2])

print('\nMatrix A2:')
print('U = ', np.linalg.svd(A2)[0])
print('Sigma = ', np.linalg.svd(A2)[1])
print('VH = ', np.linalg.svd(A2)[2])

print('\nMatrix A3:')
print('U = ', np.linalg.svd(A3)[0])
print('Sigma = ', np.linalg.svd(A3)[1])
print('VH = ', np.linalg.svd(A3)[2])

print('\nMatrix A4:')
print('U = ', np.linalg.svd(A4)[0])
print('Sigma = ', np.linalg.svd(A4)[1])
print('VH = ', np.linalg.svd(A4)[2])

# Exercise 8
print('\n-------Exercise 8-------')
B1 = np.array([[-18,13,-4,4],[2,19,-4,12],[-14,11,-12,8],[-2,21,4,8]])
B2 = np.array([[6,-8,-4,5,-4],[2,7,-5,-6,4],[0,-1,-8,2,2],[-1,-2,4,4,-8]])

print('Matrix B1:')
print('U = ', np.linalg.svd(B1)[0])
print('Sigma = ', np.linalg.svd(B1)[1])
print('VH = ', np.linalg.svd(B1)[2])

print('\nMatrix B2:')
print('U = ', np.linalg.svd(B2)[0])
print('Sigma = ', np.linalg.svd(B2)[1])
print('VH = ', np.linalg.svd(B2)[2])

