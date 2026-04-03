from typing import List

class Solution:
    def canJump(self, nums: List[List[int]])->bool:
        
        pointer = len(nums) - 1
        
        for i in range(len(nums) - 1,-1,-1):
            if nums[i] + i >= pointer:
                pointer = i
        return (pointer == 0)
        
# time complexity: O(n)
# space complexity: O(1)
sol = Solution()
nums = [1,2,0,1,0]
print(sol.canJump(nums))
nums = [1,2,1,0,1]
print(sol.canJump(nums))
                