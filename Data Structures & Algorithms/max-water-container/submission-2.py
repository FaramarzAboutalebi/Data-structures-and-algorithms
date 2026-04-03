from typing import List

class Solution:
    def maxArea(self, heights: List[int])->int:
        
        maxArea = 0
        l,r = 0, len(heights) - 1
        
        while l < r:
            area = min(heights[l],heights[r]) * (r-l)
            maxArea = max(maxArea, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea
        
# space complexity: O(n)
# time complexity: O(1)

height = [1,7,2,5,4,7,3,6]
print(Solution().maxArea(height))

            
        
        
        
        
        