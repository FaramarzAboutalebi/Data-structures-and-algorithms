from typing import List

class Solution:
    def maxArea(self,heights: List[int])->int:
        
        maxAmount = 0
        
        l, r = 0, len(heights) - 1
        
        while l < r:
            amount = (r-l) * min(heights[l],heights[r])
            maxAmount = max(maxAmount,amount)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxAmount
# time complexity: O(n)
# space complexity: O(1)
height = [1,7,2,5,4,7,3,6]        
print(Solution().maxArea(height))
height = [2,2,2]
print(Solution().maxArea(height))
            