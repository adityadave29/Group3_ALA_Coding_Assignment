#q5

#function that will return the sum of the diagonal elements
def printDiagonalSums(mat, n):
    principal = 0
    secondary = 0;
    for i in range(0, n):
        for j in range(0, n):

            # Condition for principal diagonal
            if (i == j):
                principal += mat[i][j]

            # Condition for secondary diagonal
            if ((i + j) == (n - 1)):
                secondary += mat[i][j]

    #print("Principal Diagonal:", principal)
    #print("Secondary Diagonal:", secondary)
    return principal


import math
A=[]
B=[]
R=int(input("enter the number of rows:"))
C=int(input("enter the number of columns:"))
print("enter the elements of the arr:")
for i in range (R):
    a=[]
    for j in range (C):
        a.append(int(input()))
    A.append(a)


print("the matrix A is:")
for i in range (R):
    for j in range (C):
        print(A[i][j],end=" ")
    print()

#finding the tranpose of the matrix
for i in range (R):
    b=[]
    for j in range (C):
        b.append(A[j][i])
    B.append(b)


print("the transpose of A is")
for i in range (C):
    for j in range (R):
        print(B[i][j],end=" ")
    print()


#initialising result matrix with 0
Result=[]
for i in range (R):
    result=[]
    for j in range (C):
        result.append(0)
    Result.append(result)


#doing matrix multiplication of A and A transpose
for i in range(R):
    for j in range(C):
        for k in range(len(B)):
            Result[i][j] += A[i][k] * B[k][j]


print("result")
for i in range (R):
    for j in range (C):
        print(Result[i][j],end=" ")
    print()

c=printDiagonalSums(Result,R)
#print("sum of diagonal elements is ",c)

print("the norm of the matrix is ",math.sqrt(c))