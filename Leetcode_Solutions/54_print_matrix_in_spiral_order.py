# advanced python

# leetcode : 54 - print matrix in spiral manner

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n=len(matrix)
        m=len(matrix[0])

        top=0
        bottom=n-1
        left=0
        right=m-1
        l1=[]


        while top<=bottom and left<=right:
            for i in range(left, right+1):
                l1.append(matrix[top][i])
            top+=1
            for i in range(top, bottom+1):
                l1.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right, left-1,-1):
                    l1.append(matrix[bottom][i])
                bottom-=1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    l1.append(matrix[i][left])
                left+=1
        return l1