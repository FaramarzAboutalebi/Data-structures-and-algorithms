from typing import List

class Solution:
    def maxProduct(self, nums: List[int])->int:
        
        res = max(nums)
        
        curMin,curMax = 1,1
        
        for n in nums:
            if n == 0:
                curMin = 1
                curMax = 1
            temp = curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(n * temp, n * curMin, n)
            
            res = max(res,curMax)
        return res
    
'''
Example 1:

Input: nums = [1,2,-3,4]
Output: 4

Example 2:

Input: nums = [-2,-1]
Output: 2
'''
sol = Solution() 

nums = [1,2,-3,4]
print(sol.maxProduct(nums))

nums = [-2,-1]
print(sol.maxProduct(nums))


        
# time complexity:  O(n)
# space complexity: O(1)
            