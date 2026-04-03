from typing import List

class Solution:
    def missingNumber(self, nums: List[int])->int:
        
        xor = len(nums)
        
        for i in range(len(nums)):
            xor ^= (i ^ nums[i])
        return xor
# time complexity: O(n)
# space complexity: O(1)
sol = Solution()
nums = [1,2,3]
print(sol.missingNumber(nums))

nums = [0,2]
print(sol.missingNumber(nums))