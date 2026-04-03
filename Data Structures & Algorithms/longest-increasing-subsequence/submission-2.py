from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int])->int:
        
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(1+dp[j],dp[i])
                    res = max(res, dp[i])
        return res
# time complexity: O(n^2)
# space complexity: O(n)
nums = [9,1,4,2,3,3,7]
print(Solution().lengthOfLIS(nums))