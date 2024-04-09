# 520H0392 - Truong Phuc Nguyen


import numpy as np
import sympy as sp
from scipy.linalg import orth 


# Exercise 1
print('----------Exercise 1----------')

# Exercise 1c
v1 = np.array([1,1,2,2])
v2 = np.array([2,3,5,6])
v3 = np.array([2,-1,3,6])
w = np.array([-1,6,1,-4])

A = np.column_stack((v1,v2,v3))

def isLinearComb(A,w):
    if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(np.column_stack((A,w))):
        return True
    else:
        return False
    

print('Exercise 1c\nw is a linear combination of v1,v2,v3:',isLinearComb(A,w))

# Exercise 1d
v1 = np.array([1,2,3,4])
v2 = np.array([-1,0,1,3])
v3 = np.array([0,5,-6,8])
v4 = np.array([1,15,-12,8])

w = np.array([0,-6,17,11])

A = np.column_stack((v1,v2,v3,v4))
 
print('\nExercise 1d\nw is a linear combination of v1,v2,v3,v4:',isLinearComb(A,w))

# Exercise 2
print('\n----------Exercise 2----------')

# Exercise 2a
v1 = np.array([[1,-2,0]]).T
v2 = np.array([[0,-4,1]]).T
v3 = np.array([[1,-1,1]]).T

A = np.column_stack((v1,v2,v3))

res = sp.Matrix(A).rref()

print('Exercise 2a:\nThe vectors are linearly independent:',len(res[1]) == len(A[0]))
      
# Exercise 2d
v1 = np.array([[0,0,1,2,3]]).T
v2 = np.array([[0,0,2,3,1]]).T
v3 = np.array([[1,2,3,4,5]]).T
v4 = np.array([[2,1,0,0,0]]).T
v5 = np.array([[-1,-3,-5,0,0]]).T

A = np.column_stack((v1,v2,v3,v4,v5))

res = sp.Matrix(A).rref()

print('\nExercise 2d:\nThe vectors are linearly independent:',len(res[1]) == len(A[0]))

# Exercise 3
print('\n----------Exercise 3----------')

C = np.array([[1,0,2,3],[4,-1,0,2],[0,-1,-8,-10]])

# Exercise 3a: find a basis for col(C)
res = sp.Matrix(C).rref()

print('Basis for the col(C):\n',C[:,list(res[1])])



# Exercise 3b
res = sp.Matrix(C.T).rref()

print('\nBasis for the row(C):\n',(C.T[:,list(res[1])]).T)


# Exercise 4
print('\n----------Exercise 4----------')

A2 = np.array([[1,0,2,3],[4,-1,0,2],[0,-1,-8,-10]])

res = sp.Matrix(A2).rref()
temp = np.hstack(sp.Matrix(A2).nullspace())

print('\nExercise 4a\nv1:',temp[:,0],'\nv2:',temp[:,1])


# Exercise 5
print('\n----------Exercise 5----------')

# Exercise 5a
w = np.array([[1,1,-1,-3]]).T 
A = np.array([[7,6,-4,1],[-5,-1,0,-2],[9,-11,7,-3],[19,-9,7,1]])


# Exercise 5b
w1 = np.array([[1,2,1,0]]).T
A1 = np.array([[-8,5,-2,0],[-5,2,1,-2],[10,-8,6,-3],[3,-2,1,0]])


def isColumnSpace(A,w):
    if np.linalg.matrix_rank(A) == np.linalg.matrix_rank(np.column_stack((A,w))):
        return True
    else:
        return False
    
def isNullSpace(A,w):
    if np.allclose(np.dot(A,w),0):
        return True
    else:
        return False
    
def checkSpace(A,w):
    if isColumnSpace(A,w) and isNullSpace(A,w):
        print('Both column space and null space')
    elif isColumnSpace(A,w):
        print('Column space')
    elif isNullSpace(A,w):
        print('Null space')
    else:
        print('Neither column space nor null space')

print('Exercise 5a')
checkSpace(A,w)

print('\nExercise 5b')
checkSpace(A1,w1)



# # Exercise 6: Let a1, a2,..a5 donate the columns of the matrix A, where:
print('\n----------Exercise 6----------')

A = np.array([[5,1,2,2,0],[3,3,2,-1,-12],[8,4,4,-5,12],[2,1,1,0,-2]])

# B = [a1a2a4] -> index 013
B = A[:,[0,1,3]]

res = sp.Matrix(B).rref()
print('Rank of B:',np.linalg.matrix_rank(B))
print('Rank of B|a3:',np.linalg.matrix_rank(np.column_stack((B,A[:,2]))))
print('Rank of B|a5:',np.linalg.matrix_rank(np.column_stack((B,A[:,4]))))

print('\na3 and a5 are in the column space of B because they are linear combination of the columns of B')


# Exercise 7
print('\n----------Exercise 7----------')

v1 = np.array([[1,0,2]]).T
v2 = np.array([[0,1,4]]).T
v3 = np.array([[2,2,4]]).T

A = np.column_stack((v1,v2,v3))

res = sp.Matrix(A).rref()

print('The dimension of the span:',len(res[1]))
print('The basis for the span:',A[:,list(res[1])])


# Exercise 9: write a function to show that {u1,u2,...un} is an orthogonal set

print('\n----------Exercise 9----------')


def isOrthogonal(U):
    for i in range(len(U)):
        for j in range(i+1,len(U)):
            if np.dot(U[i],U[j]) != 0:
                return False
    return True

U = np.array([[1,2,3],[1,1,-1],[5,-4,1]])
U1 = np.array([[3,1,1],[-1,2,1],[-1/2,2,7/2]])


print('The set is orthogonal:',isOrthogonal(U))
print('The set is orthogonal:',isOrthogonal(U1))


# Exercise 10: let y and u vector. write a function to find the orthogonal projection of y on u

print('\n----------Exercise 10----------')

def orthogonalProjection(y,u):
    return np.dot(y,u)/np.dot(u,u)*u

y = np.array([7,6])
u = np.array([4,2])

print('The orthogonal projection of y on u:',orthogonalProjection(y,u))


# Exercise 11: Let a matrix mxn, write a function to check that has orthonormal columns

print('\n----------Exercise 11----------')


def isOrthonormal(U):
    return np.allclose(np.eye(U.shape[1]),np.dot(U.T,U))

a = np.pi/2
U = np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])

print('The columns are orthonormal:',isOrthonormal(U))


# Exercise 12: use Gram-Schmidt process to produce an orthogonal basis for column space of
A = np.array([[-10,13,7,-11],[2,1,-5,3],[-6,3,13,-3],[16,-16,-2,5],[2,1,-5,-7]])

print('\n----------Exercise 12----------')



def orthogonalBasis(A):
    return orth(A)

C = np.array([[2,0,0],[0,5,0]])

print('Orthogonal basis for column space of A:\n',orthogonalBasis(A))
print('\nOrthogonal basis for column space of C:\n',orthogonalBasis(C))

