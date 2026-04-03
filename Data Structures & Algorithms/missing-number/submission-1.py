from typing import List
class Solution:
    def missingNumber(self, nums: List[int])->int:
        # res = 0
        # for i in range(len(nums) + 1):
        #     if i < len(nums):
        #         res += (i-nums[i])
        #     else:
        #         res += i
        # return res
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res
# time complexity: O(n)
# space complexity: O(1)
sol = Solution()
nums = [1,0,3]
print(sol.missingNumber(nums))
            