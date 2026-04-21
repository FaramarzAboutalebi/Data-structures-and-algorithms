from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]):
        
        isFistRowZero = False
        Rows,Cols = len(matrix), len(matrix[0])
    
        
        for r in range(Rows):
            for c in range(Cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        isFistRowZero = True
                    else:
                        matrix[0][c] = 0
                        matrix[r][0] = 0
                
                    
        for r in range(1, Rows):
            for c in range(1, Cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                    
        if matrix[0][0] == 0:
            for r in range(1,Rows):
                matrix[r][0] = 0
        
        if isFistRowZero:
            for c in range(Cols):
                matrix[0][c] = 0

# time complexity: O(n * m)
# space complexity: O(1)         
            
                    
                    