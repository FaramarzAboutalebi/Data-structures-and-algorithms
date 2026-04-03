from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]])->List[int]:
        
        left,right = 0, len(matrix[0])-1
        top,bottom = 0, len(matrix)-1
        res = []
        while left <= right and top <= bottom:
            
            for c in range(left,right+1):
                res.append(matrix[top][c])
            top += 1
            for r in range(top,bottom+1):
                res.append(matrix[r][right])
            right -= 1
            
            if not (left <= right and top <= bottom):
                break
            
            for c in range(right, left-1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1
            
            for r in range(bottom, top-1,-1):
                res.append(matrix[r][left])
            left += 1
        return res
# space complexity: O(m*n)
# space complexity: O(m*n)
matrix = [[1,2],[3,4]]
print(Solution().spiralOrder(matrix))

                