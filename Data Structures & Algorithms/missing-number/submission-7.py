from typing import List

class Solution:
    def missingNumber(self, nums: List[int])->int:
        
        res = len(nums)
        
        for i in range(len(nums)):
            res ^= (i ^ nums[i])
        
        return res

# time complexity: O(n)
# space complexity: O(1)

nums = [2,0,1]
sol = Solution()
print(sol.missingNumber(nums))