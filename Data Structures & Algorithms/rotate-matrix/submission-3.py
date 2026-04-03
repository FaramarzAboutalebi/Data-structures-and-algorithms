from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]])->None:
        
        l, r = 0, len(matrix) - 1
        
        while l <= r:
            top, bottom = l, r
            for i in range(r-l):
                temp = matrix[top][l+i]
                
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top+i][r]
                matrix[top+i][r] = temp
                
            l += 1
            r -= 1
            
# time complexity: O(n^2) 
# space complexity: O(1)

matrix = [[1,2],[3,4]]
Solution().rotate(matrix)
res = [
  [3,1],
  [4,2]
]
print(matrix == res)

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
Solution().rotate(matrix)
res = [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
print(matrix == res)