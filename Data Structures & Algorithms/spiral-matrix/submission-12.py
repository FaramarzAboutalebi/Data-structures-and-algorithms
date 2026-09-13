class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ROWS,COLS = len(matrix),len(matrix[0])
        left,right = 0, COLS-1
        top, bottom = 0, ROWS-1
        res = []
        while left <= right and top <= bottom:

            for c in range(right-left+1):
                res.append(matrix[top][left+c])

            top += 1

            for r in range(bottom-top+1):
                res.append(matrix[top+r][right])
            
            right -= 1

            if not (left <= right and top <= bottom):
                break
            
            for c in range(right-left+1):
                res.append(matrix[bottom][right-c])
            
            bottom -= 1

            for r in range(bottom-top+1):
                res.append(matrix[bottom-r][left])
            left += 1
        return res
                

# time complexity: O(n*m)
# space complexity: O(n*m)