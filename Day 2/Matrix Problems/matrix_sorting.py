import numpy as np

matrix = np.array([[3,3,1,1],[2,2,1,2],[1,1,1,2]])
list1=[]
for i in matrix:
    for j in i:
        list1.append(j)
sorted_list = sorted(list1)
index=0
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        matrix[i,j] = sorted_list[index]
        index+=1
print(matrix)