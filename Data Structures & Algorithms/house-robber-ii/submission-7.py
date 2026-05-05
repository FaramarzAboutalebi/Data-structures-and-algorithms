from typing import List

class Solution:
    def rob(self, nums: List[int])->int:
        # time complexity: O(n)
        # space complexity: O(1)
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_helper(nums[0:len(nums)-1]),self.rob_helper(nums[1:]))
        
    def rob_helper(self, subNums):
        # time complexity: O(n)
        # space complexity: O(1)
        
        left, right = 0,0
        
        for n in subNums:
            right, left = max(right, left + n),right
        return right
            
            