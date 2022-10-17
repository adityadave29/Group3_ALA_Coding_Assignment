from math import sqrt
row = 2
col = 2

def frobeniusNorm(mat):

	sumSq = 0
	for i in range(row):
		for j in range(col):
			sumSq += pow(mat[i][j], 2)

	res = sqrt(sumSq)
	return round(res, 5)


mat = [ [ 1, 2 ], [ 3, 4 ] ]

print(frobeniusNorm(mat))