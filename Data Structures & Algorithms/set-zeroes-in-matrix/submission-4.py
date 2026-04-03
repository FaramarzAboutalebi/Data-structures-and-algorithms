from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]])->None:
        
        Rows, Cols = len(matrix), len(matrix[0])
        
        firstRowZero = False
        
        for r in range(Rows):
            for c in range(Cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        firstRowZero = True
                    else:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
        for r in range(1, Rows):
            for c in range(1, Cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                    
        if matrix[0][0] == 0:
            for r in range(1,Rows):
                matrix[r][0] = 0
                
        if firstRowZero:
            for c in range(Cols):
                matrix[0][c] = 0
                
# time complexity: O(n * m)
# space complexity: O(1)

sol = Solution()

matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
sol.setZeroes(matrix)
print(matrix)