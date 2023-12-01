import numpy as np

vector = [10, 20]
matrix = [[1, 4],
          [-5, 8]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        matrix[i][j] = abs(matrix[i][j] * vector[j])
mat = np.matrix(matrix)
with open('file.txt', 'wb') as f:
    for line in mat:
        np.savetxt(f, line, fmt='%.2f\t')
