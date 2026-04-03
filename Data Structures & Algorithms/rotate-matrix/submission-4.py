from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]])->None:
        
        left,right = 0, len(matrix)-1
        
        while left < right:
            top, bottom = left,right
            
            for i in range(right-left):
                
                temp = matrix[top][left+i]
                
                matrix[top][left+i] = matrix[bottom-i][left]
                
                matrix[bottom-i][left] = matrix[bottom][right-i]
                
                matrix[bottom][right-i] = matrix[top+i][right]
                
                matrix[top+i][right] = temp
                
            left += 1
            right -= 1

# time complexity: O(n^2)
# space complexity: O(1)

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]         
Solution().rotate(matrix)
print(matrix)