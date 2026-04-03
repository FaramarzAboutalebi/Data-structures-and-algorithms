class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # time complexity: O(n)
        # space complexity: O(1)
        # res = 0
        # for i in range(len(nums)+1):
        #     res += i 
        #     if i < len(nums):
        #         res -= nums[i]
        # return res
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res