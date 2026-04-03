
from typing import List

class Solution:
    def canJump(self,nums: List[int])->bool:
        
        goal = len(nums)-1
        
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        
        
sol = Solution()
nums = [1,2,0,1,0]
print(sol.canJump(nums))

nums = [1,2,1,0,1]
print(sol.canJump(nums))
        
        
        
        
# time complexity: O(n)
# space complexity: O(1)
    
        