# 520H0392 - Truong Phuc Nguyen

import numpy as np


# Exercise 1: Find 1-norm
# np.linalg.norm(A1,1)
print('----------Exercise 1----------')
# write function to find 1 norm

# Exercise 1a
A1 = np.array([[1, -7], [-2, -3]])
print('\n1-norm A1=',np.max(np.sum(np.abs(A1), axis=0)))

# Exercise 1b
A2 = np.array([[-2,8],[3,1]])
print('\n1-norm A2=',np.max(np.sum(np.abs(A2), axis=0)))

# Exercise 1c
A3 = np.array([[2,-8],[3,1]])
print('\n1-norm A3=',np.max(np.sum(np.abs(A3), axis=0)))

# Exercise 1d
A4 = np.array([[2,3],[1,-1]])
print('\n1-norm A4=',np.max(np.sum(np.abs(A4), axis=0)))

# Exercise 1e
A5 = np.array([[5,-4,2],[-1,2,3],[-2,1,0]])
print('\n1-norm A5=',np.max(np.sum(np.abs(A5), axis=0)))
      



# Exercise 2: Find infinity-norm
# 
print('\n----------Exercise 2----------')


# Exercise 2a
B1 = np.array([[1,-7],[-2,-3]])
print('\nInfinity-norm B1=',np.linalg.norm(B1, np.inf))

# Exercise 2b
B2 = np.array([[3,6],[1,0]])
print('\nInfinity-norm B2=',np.linalg.norm(B2, np.inf))

# Exercise 2c
B3 = np.array([[5,-4,2],[-1,2,3],[-2,1,0]])
print('\nInfinity-norm B3=',np.linalg.norm(B3, np.inf))

# Exercise 2d
B4 = np.array([[3,6,-1],[3,1,0],[2,4,-7]])
print('\nInfinity-norm B4=',np.linalg.norm(B4, np.inf))

# Exercise 2e
B5 = np.array([[-3,0,0],[0,4,0],[0,0,2]])
print('\nInfinity-norm B5=',np.linalg.norm(B5, np.inf))





# Exercise 3: Find Frobenius-norm
# np.linalg.norm(C1, 'fro')
print('\n----------Exercise 3----------')

# Exercise 3a
C1 = np.array([[5,-4,2],[-1,2,3],[-2,1,0]])
print('\nFrobenius-norm C1=',np.linalg.norm(C1, 'fro'))

# Exercise 3b
C2 = np.array([[1,7,3],[4,-2,-2],[-2,1,1]])
print('\nFrobenius-norm C2=',np.linalg.norm(C2, 'fro'))

# Exercise 3c
C3 = np.array([[2,3],[1,-1]])
print('\nFrobenius-norm C3=',np.linalg.norm(C3, 'fro'))
      




# Exercise 4: Find angle between two vectors
# np.across = cos angle, np.degrees = rad -> degree
print('\n----------Exercise 4----------')

def angle(u,v):
    return np.arccos(np.dot(u,v)/(np.linalg.norm(u)*np.linalg.norm(v)))

# Exercise 4a
u = np.array([1,1])
v = np.array([0,1])
print('\nExercise 4a \nAngle between u and v:',np.degrees(angle(u,v)))

# Exercise 4b
u = np.array([1,0])
v = np.array([0,1])
print('\nExercise 4b\nAngle between u and v:',np.degrees(angle(u,v)))

# Exercise 4c
u = np.array([-2,3])
v = np.array([1/2,-1/2])
print('\nExercise 4c\nAngle between u and v:',np.degrees(angle(u,v)))





# Exercise 5
print('\n----------Exercise 5----------')

# Exercise 5a
u = np.array([2,3])
print('\nExercise 5a\nUnit vector of u:',u/np.linalg.norm(u))

# Exercise 5b
u = np.array([1,2,3])
print('\nExercise 5b\nUnit vector of u:',u/np.linalg.norm(u))

# Exercise 5c
u = np.array([1/2,-1/2,1/4])
print('\nExercise 5c\nUnit vector of u:',u/np.linalg.norm(u))

# Exercise 5d
u = np.array([np.sqrt(2),2,-np.sqrt(2),np.sqrt(2)])
print('\nExercise 5d\nUnit vector of u:',u/np.linalg.norm(u))





# Exercise 6
print('\n----------Exercise 6----------')

v1 = np.array([1,2,3])
s2 = np.array([7,4,3])
s3 = np.array([2,1,9])

print('\nDistance between v1 and s2:',np.linalg.norm(v1-s2))
print('\nDistance between v1 and s3:',np.linalg.norm(v1-s3))
print('\nDistance between s2 and s3:',np.linalg.norm(s2-s3))





# Exercise 7
print('\n----------Exercise 7----------')

E = np.array([[80,98,99,85,106,94],[71,92,76,95,100,92],[124,163,140,160,176,161]])

A = np.array([[1,2,3],[2,1,2],[3,2,4]])
A_inv = np.linalg.inv(A)

D = np.matmul(E.T,A_inv)

def decode(D):
    result = ""
    for i in range(0,6):
        for j in range(0,3):
            result = result + chr(int(round(D[i,j],0)) + 61)
    return result

print('\nDecoded message:',decode(D))


# Exercise 8
print('\n----------Exercise 8----------')

A = np.array([[3,4,5],[1,3,1],[1,1,2]])

msg1 = "ATTACK"

D = np.full((3,2),30)

newD = np.array([[ord(msg1[0])-61,ord(msg1[1])-61,ord(msg1[2])-61],
                  [ord(msg1[3])-61,ord(msg1[4])-61,ord(msg1[5])-61]])

E = np.matmul(A,newD.T)
print('Encoded message 1:\n',E)



msg2 = "LINEAR ALGEBRA LABORATORY "

newD2 = np.array([  [ord(msg2[0])-61,ord(msg2[1])-61,ord(msg2[2])-61],  
                    [ord(msg2[3])-61,ord(msg2[4])-61,ord(msg2[5])-61],
                    [30,ord(msg2[7])-61,ord(msg2[8])-61],
                    [ord(msg2[9])-61,ord(msg2[10])-61,ord(msg2[11])-61],
                    [ord(msg2[12])-61,ord(msg2[13])-61,30],
                    [ord(msg2[15])-61,ord(msg2[16])-61,ord(msg2[17])-61],  
                    [ord(msg2[18])-61,ord(msg2[19])-61,ord(msg2[20])-61],
                    [ord(msg2[21])-61,ord(msg2[22])-61,ord(msg2[23])-61],
                    [ord(msg2[24])-61,30,30]])

E2 = np.matmul(A,newD2.T)
print('\nEncoded message 2:\n',E2)





# Exercise 9
print('\n----------Exercise 9----------')

D = np.array([[0,4,0,0,0,2,1,3],
                [3,1,4,3,1,2,0,1],
                [3,0,0,0,3,0,3,0],
                [0,1,0,3,0,0,2,0],
                [2,2,2,3,1,4,0,2]])

def cosSimi(D):
    result = np.zeros((5,5))
    for i in range(0,5):
        for j in range(0,5):
            result[i,j] = np.dot(D[i],D[j])/(np.linalg.norm(D[i])*np.linalg.norm(D[j]))
    return result

for i in range(0,5):
    for j in range(0,5):
        print('Similarity between Doc',i+1,' and Doc',j+1,':',round(cosSimi(D)[i,j],3))





# Exercise 10
print('\n----------Exercise 10----------')

A = np.array([[1.0,0.5,0.3,0,0,0],
                [0.5,1.0,0,0,0,0],
                [0,1.0,0.8,0.7,0,0],
                [0,0.9,1.0,0.5,0,0],
                [0,0,0,1.0,0,1.0],
                [0,0,0,0,0.7,0],
                [0.5,0,0.7,0,0,0.9],
                [0,0.6,0,1.0,0.3,0.2]])

q = np.array([0,0,0.7,0.5,0,0.3])

def nearestDoc(A,q):
    result = np.zeros(8)
    for i in range(0,8):
        result[i] = np.dot(A[i],q)/(np.linalg.norm(A[i])*np.linalg.norm(q))
    return result

print('\nNearest document to q = ',np.argmax(nearestDoc(A,q))+1)
