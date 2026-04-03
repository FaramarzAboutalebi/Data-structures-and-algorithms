from typing import List

class Solution:
    def maxSubArray(self, nums: List[int])->int:
        
        maxSum = float("-inf")
        curSum = 0
        
        for n in nums:
            if curSum < 0: 
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)
            
        return maxSum
        
# time complexity: O(n)
# space complexity: O(1)

nums = [2,-3,4,-2,2,1,-1,4]        
print(Solution().maxSubArray(nums))

nums = [-1]
print(Solution().maxSubArray(nums))
