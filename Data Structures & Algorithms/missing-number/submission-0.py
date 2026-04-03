from typing import List

# class Solution:
#     def missingNumber(self, nums: List[int]):
#         res = len(nums)
#         for i in range(len(nums)):
#             res += i - nums[i]
#         return res
    
class Solution:
    def missingNumber(self, nums: List[int]):
        xorr = len(nums)
        
        for i in range(len(nums)):
            xorr ^= i ^ nums[i]
        return xorr
# time complexity: O(n)
# space complexity: O(1)
sol = Solution()
nums = [0,2,3]
print(sol.missingNumber(nums))