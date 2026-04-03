from typing import List

class Solution:
    def rob(self, nums: List[int])-> int:
        if len(nums) == 1:
            return nums[0]
        return max (self.maxMoneyOfSub(nums[:len(nums)-1]),self.maxMoneyOfSub(nums[1:len(nums)]))
        
        
        
    
    def maxMoneyOfSub(self, nums: List[int])-> int:
        rob1,rob2 = 0,0
        
        for n in nums:
            temp = rob2
            rob2 = max(rob2,rob1+n)
            rob1 = temp
        return rob2
        
sol = Solution()
nums = [2,9,8,3,6]
res = sol.rob(nums)
print(res)
nums = [3,4,3]
res = sol.rob(nums)
print(res)

            
            
        