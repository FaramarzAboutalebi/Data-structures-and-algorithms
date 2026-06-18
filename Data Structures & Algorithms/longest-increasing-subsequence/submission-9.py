class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        dp = [1] * len(nums)
        res = 1

        for i in range(len(nums)-2,-1,-1):

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    res = max(res, dp[i])
        return res
        
# time complexity: O(n^2)
# space complexity: O(n)