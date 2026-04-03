class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = max(nums)
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum,curSum)
        return maxSum


# time complexity: O(n)
# space complexity: O(1)
sol = Solution()
nums = [2,-3,4,-2,2,1,-1,4]
print(sol.maxSubArray(nums))