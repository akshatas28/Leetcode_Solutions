# leetcode 48 - rotate image

import copy

matrix = [ [1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16] ]

matrix1=copy.deepcopy(matrix)

i1=0
j = len(matrix[0])-1

while i1<len(matrix):
    i=0
    j1=0
    while i<len(matrix[0]):
        matrix[i][j]=matrix1[i1][j1]
        i+=1
        j1+=1
    i1+=1
    j-=1

print(matrix)