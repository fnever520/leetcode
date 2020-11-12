'''
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
'''
"""
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
"""
def rotate(matrix):
        n = len(matrix)
        
        for i in range(n):
            for j in range(i,n): ## this do transpose 00, 01, 02, 11, 12, 22 
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        for i in range(n):
            for j in range(n//2): # swap the two pointer based on the centre
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = temp

        return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))