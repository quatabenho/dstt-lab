import numpy as np

# 520H0392 - Truong Phuc Nguyen
# Exercise 1

print('Exercise 1: Create new matrix')
x = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5,6])
c = np.arange(1,31)
d = np.arange(1,26)

# Exercise 1a
print('\nExercise 1a')
print('A = ',(np.tile(x,(5,1)).T))

# Exercise 1b
print('\nExercise 1b')
print('B = ',(np.tile(b,(6,1))))

# Exercise 1c
print('\nExercise 1c')
print('C = ',(c.reshape(6,5).T))

# Exercise 1d
print('\nExercise 1d')
print('D = ',(d.reshape(5,5)))



# Exercise 2
print('\nExercise 2: Create random 5x6 matrix')
print('E =',np.random.randint(1,100,(5,6)))



# Exercise 3
A = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])

print('\nExercise 3')
print('B = ',np.flip(A,1))



# Exercise 4
print('\nExercise 4')
print('B = ',np.flip(A,0))



# Exercise 5
print('\nExercise 5')

Y = np.array([[1,2,16,31,22],
              [2,8,12,21,23],
              [4,9,11,14,25],
              [3,6,10,16,34]])


# Exercise 5a
print('\nExercise 5a')
print('x = ',Y[1,1:4])


# Exercise 5b
print('\nExercise 5b')
print('y = ',Y[0:4,2:3])


# Exercise 5c
print('\nExercise 5c')
print('A = ',Y[1:3,1:4])


# Exercise 5d
print('\nExercise 5d')
print('B = ',Y[0:4:1,0:5:2])


# Exercise 5e
print('\nExercise 5e',) 
print('C = ',Y[1:,[0,2,3,4]])


# Exercise 5f
print('\nExercise 5f')
print('D =', Y[Y > 12])



# Exercise 6
A = np.array([[2,4,1],[6,7,2],[3,5,9]])
print('\nExercise 6')


# Exercise 6a: first row
print('\nExercise 6a: x1 = ',A[0,:])


# Exercise 6b: last 2 rows
print('\nExercise 6b: Y = ',A[1:,:])



# Exercise 7
print('\nExercise 7')
A = np.array([[2,7,9,7],[3,1,5,6],[8,1,2,5]])

# Exercise 7a: Vector B: even numbered columns of A
print('\nExercise 7a: B = ',A[:,1::2])


# Exercise 7b: Vector C: odd numbered rows of A
print('\nExercise 7b: C = ',A[0::2,:])


# Exercise 7c: Vector D: Convert A to a 4x3 matrix
print('\nExercise 7c: D = ',A.reshape(4,3))