# leetcode 73 - set matrix zeros

matrix = [ [7,10,29,3] , [1,20,0,4] , [19,0,6,11] , [4,27,14,7] ]
    
row=len(matrix)
col=len(matrix[0])

rowtracker=[0]*row
coltracker=[[0]]*col

for i in range(row):
    for j in range(col):
        if matrix[i][j]==0:
            rowtracker[i]=-1
            coltracker[j]=-1
print(rowtracker, coltracker)

for i in range(row):
    for j in range(col):
        if rowtracker[i]==-1:
            matrix[i][j]=0
        if coltracker[j]==-1:
            matrix[i][j]=0
print(matrix)