from typing import List

class Solution:
    def setZeroes(self,matrix: List[List[int]])->None:
        
        ROWS,COLS = len(matrix),len(matrix[0])
        firstROWZero = False
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        firstROWZero = True
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
          
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        if firstROWZero:
            for c in range(COLS):
                matrix[0][c] = 0
     
sol = Solution()

matrix = [
  [0,1],
  [1,0]
]
sol.setZeroes(matrix)
print(matrix)
    # Time complexity: O(n*m)
    # space complexity: O(1)
                
            
            
            
            
            
            
            
        
