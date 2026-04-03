from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int])->int:
        
        n = len(nums)
        res = 1
        dp = [1] * n
        
        for i in range(n-2,-1,-1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j]) 
                    res = max(res, dp[i])
        return res
        
# time complexity: O(n^2)
# space complexity: O(n)

sol = Solution()
nums = [9,1,4,2,3,3,7]
print(sol.lengthOfLIS(nums))

nums = [0,3,1,3,2,3]
print(sol.lengthOfLIS(nums))