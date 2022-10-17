def mulMat(matrix1, matrix2, r1, r2, c1, c2):
	answer = [[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[0, 0, 0, 0]]

	for i in range(0, r1):
		for j in range(0, c2):
			for k in range(0, r2):
				answer[i][j] += matrix1[i][k] * matrix2[k][j]

	print("Multiplication of given two matrices is:")
	for i in range(0, r1):
		for j in range(0, c2):
			print(answer[i][j], end=" ")
		print("\n", end="")

if __name__ == '__main__':
	R1 = 4
	R2 = 4
	C1 = 4
	C2 = 4

	mat1 = [[1, 1,1,1],
		[2, 2,2,2],
		[3, 3,3,3],
		[4, 4,4,4]]
	mat2 = [[1, 1,1,1],
		[2, 2,2,2],
		[3, 3,3,3],
		[4, 4,4,4]]

	if C1 != R2:
		print("The number of columns in Matrix-1 must be equal to the number of rows in " + "Matrix-2", end='')
		print("\n", end='')
		print("Please update MACROs according to your array dimension in #define section", end='')
		print("\n", end='')
	else:
		mulMat(mat1, mat2, R1, R2, C1, C2)
