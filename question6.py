from random import randint

def displayMatrix(matrix):
  for row in matrix:
    print('[', end='')
    for cell in row:
      print('{0:>7.2f}'.format(cell + 0), end=' ')
    print(']')
  print()

def randomMatrix(rows, cols):
  m = []
  for i in range(rows):
    row = []
    for i in range(cols):
      row.append(randint(0, 10))
    m.append(row)
  return m

def leadingOne(matrix, i):
  if matrix[i][i] == 0:
    return
  matrix[i] = [cell / matrix[i][i] for cell in matrix[i]]

def pivot(matrix, i):
  for r, row in enumerate(matrix):
    if r != i:
      scale = -1 * row[i]
      matrix[r] = [curr + scale * other for curr, other in zip(matrix[r], matrix[i])]

def rref(matrix):
  for i in range(len(matrix)):
    leadingOne(matrix, i)
    pivot(matrix, i)
  return matrix

m = randomMatrix(5, 8)

print('Original matrix:')
displayMatrix(m)
print('RREF form:')
displayMatrix(rref(m))