from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        curSum = 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            res = max(res,curSum)
            
        return res
sol = Solution()

nums = [2,-3,4,-2,2,1,-1,4]
# Output: 8
print(sol.maxSubArray(nums))

nums = [-1]
#Output: -1
print(sol.maxSubArray(nums))