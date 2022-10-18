A=[]
R=int(input("enter the number of rows:"))
C=int(input("enter the number of columns:"))
print("enter the array elements below:")
for i in range(R):
    a =[]
    for j in range(C):
         a.append(int(input()))
    A.append(a)
n=3
count2=0
for i in range (R):
    count=0
    for j in range (C):
        if(A[i][j]==0):
            count=count+1
    if(count==n):
        count2=count2+1
rank=n-count2
print("the rank of the matrix is ",rank)