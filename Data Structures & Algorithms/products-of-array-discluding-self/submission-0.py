from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int])->List[int]:
        
        output = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
# time complexity: O(n)
# space complexity: O(n)
nums = [-1,0,1,2,3]
print(Solution().productExceptSelf(nums) == [0,-6,0,0,0])

nums = [1,2,4,6]
print(Solution().productExceptSelf(nums) == [48,24,12,8])
            