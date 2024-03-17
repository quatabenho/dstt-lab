import numpy as np


# 520H0392 - Truong Phuc Nguyen


# Ecercise 8
print('-----Exercise 8-----')

sales = np.array([[12, 15, 10, 16, 12],
                  [5, 9, 14, 7, 10],
                  [8, 12, 10, 9, 15]])

price = np.array([[2],[1],[3]])

total = np.matmul(sales.T, price)

for day,total in zip(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'], total):
    print('Total sales on',day,':', total[0],'$')


# Exercise 9
print('\n-----Exercise 9-----')

T = np.array([[0.6, 0.7], [0.4, 0.3]])
p = np.array([[0.5], [0.5]])
k_values = [1, 2, 10, 100, 100000]

for k in k_values:
    p_k =  np.matmul(np.linalg.matrix_power(T, k), p)
    print(f'p_{k} = {p_k}')

# Exercise 10
print('\n-----Exercise 10-----')
A = np.array([[-1,4,8],[-9,1,2]])
B = np.array([[5,8],[0,-6],[5,6]])
C = np.array([[-4,1],[6,5]])
D = np.array([[-6,3,1],[8,9,-2],[6,-1,5]])

# Exercise 10a
print('Exercise 10a: Can not calculate because the size of A and B are not match')
# print('(AB)^T =',np.matmul(A,B.T))

# Exercise 10b
print('\nExercise 10b\n',np.matmul(B,C.T))

# Exercise 10c
print('\nExercise 10c\n',C-C.T)

# Exercise 10d
print('\nExercise 10d\n',D-D.T)

# Exercise 10e
print('\nExercise 10e\n',(D.T).T)

# Exercise 10f
print('\nExercise 10f\n',2*C.T)

# Exercise 10g
print('\nExericse 10g\n',A.T+B)

# Exercise 10h
print('\nExercise 10h\n',(A.T + B).T)

# Exericse 10i
print('\nExercise 10i\n',(2*A.T - 5*B).T)

# Exercise 10j
print('\nExercise 10j\n',(-D).T)

# Exercise 10k
print('\nExercise 10k\n',-(D.T))

# Exercise 10l
print('\nExercise 10l\n',np.matmul(C,C).T)   

# Exercise 10m
print('\nExercise 10m\n',(C.T)*(C.T))


# Exericse 11
print('\n-----Exercise 11-----')
A = np.array([[2,4,1],[6,7,2],[3,5,9]])

# Exercise 11a
print('\nExercise 11a\nA is a square matrix:',A.shape[0] == A.shape[1])  

# Exercise 11b
print('\nExercise 11b\nA is a symmetric matrix:',np.allclose(A, A.T))

# Exercise 11c
print('\nExercise 11c\nA is a skew-symmetric matrix:',np.allclose(-A, A.T))

# Exercise 11d
print('\nExercise 11d\nUpper triagular matrix of A\n',np.triu(A))

# Exercise 11e
print('\nExercise 11e\nLower triagular matrix of A\n',np.tril(A))


# Exercise 12
print('\n-----Exercise 12-----')

A = np.array([[6,0,0,5],[1,7,2,-5],[2,0,0,0],[8,3,1,8]])
B = np.array([[1,-2,5,2],[0,0,3,0],[2,-6,-7,5],[5,0,4,4]])
C = np.array([[3,5,-8,4],[0,-2,3,-7],[0,0,1,5],[0,0,0,2]])
D = np.array([[4,0,0,0],[7,-1,0,0],[2,6,3,0],[5,-8,3,0],[5,-8,4,-3]])
E = np.array([[4,0,-7,3,-5],[0,0,2,0,0],[7,3,-6,4,-8],[5,0,5,2,-3],[0,0,9,-1,2]])
F = np.array([[6,3,2,4,0],[9,0,-4,1,0],[8,-5,6,7,1],[3,0,0,0,0],[4,2,3,2,0]])

# Exercise 12a
print('\nExercise 12a\ndetA = ',np.round(np.linalg.det(A)))

# Exercise 12b
print('\nExercise 12b\ndetB = ',np.round(np.linalg.det(B)))

# Exercise 12c
print('\nExercise 12c\ndetC = ',np.round(np.linalg.det(C)))

# Exercise 12d
print('\nExercise 12d:\nCan not calculate detD because D is not square')
# print('\nExercise 12d\nDetD = ',np.round(np.linalg.det(D)))

# Exercise 12e
print('\nExercise 12e\ndetE = ',np.round(np.linalg.det(E)))

# Exercise 12f
print('\nExercise 12f\ndetF = ',np.round(np.linalg.det(F)))
      

# Exercise 13
print('\n-----Exercise 13-----')

n1 = 5
n2 = 7

A = np.random.rand(n1, n1)
B = np.random.rand(n1, n1)
C = np.random.rand(n2, n2)
D = np.random.rand(n2, n2)

print('det(A+B) = detA + detB:',np.allclose(np.linalg.det(A+B), np.linalg.det(A)+np.linalg.det(B)))
print('det(C+D) = detC + detD:',np.allclose(np.linalg.det(C+D), np.linalg.det(C)+np.linalg.det(D)))


# Exercise 14
print('\n-----Exercise 14-----')

print('detAB=(detA)(detB):', np.allclose(np.linalg.det(np.matmul(A, B)), np.linalg.det(A)*np.linalg.det(B)))
print('detCD=(detC)(detD):', np.allclose(np.linalg.det(np.matmul(C, D)), np.linalg.det(C)*np.linalg.det(D)))


# Exercise 15
print('\n-----Exercise 15-----')

A = np.array([[2,4,5/2],[-3/4,2,1/4],[1/4,1/2,2]])
B = np.array([[1,-1/2,3/4],[3/2,1/2,-2],[1/4,1,1/2]])

# Exercise 15a
print('\nExercise 15a\n(A^-1)(B^-1) = ',np.matmul(np.linalg.inv(A),np.linalg.inv(B)))

print('\n(AB)^-1 = ', np.linalg.inv(np.matmul(A,B)))

print('\n(BA)^-1 = ', np.linalg.inv(np.matmul(B,A)))

# Exericse 15b
print('\nExercise 15b\n(A^-1)^T = ',np.linalg.inv(A).T)

print('\n(A^T)^-1 = ',np.linalg.inv(A.T))