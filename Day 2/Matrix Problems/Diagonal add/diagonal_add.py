import numpy as np
matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
d_for_matrix1 =sum(matrix1[i][i] for i in range(len((matrix1))))
matrix2 =np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
d_for_matrix2 =sum(matrix2[i][i] for i in range(len((matrix2))))
print(d_for_matrix1+d_for_matrix2)