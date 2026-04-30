from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]])->None:
        
        Rows, Cols = len(matrix),len(matrix[0])
        firstRow = False
        
        for r in range(Rows):
            for c in range(Cols):
                if r == 0 and matrix[r][c] == 0:
                    firstRow = True
                elif c == 0 and matrix[r][c] == 0:
                    matrix[0][0] = 0
                elif matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, Rows):
            for c in range(1,Cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        if matrix[0][0] == 0:
            for r in range(Rows):
                matrix[r][0] = 0
        if firstRow:
            for c in range(Cols):
                matrix[0][c] = 0
                

# time complexity: O(n * m)
# space complexity: O(1)           
                    
                