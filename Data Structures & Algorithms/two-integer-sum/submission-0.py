from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int)->List[int]:
        
        numMapToIndx = {}
        
        for idx,n in enumerate(nums):
            dif = target - n
            if dif in numMapToIndx:
                return [numMapToIndx[dif],idx]
            numMapToIndx[n] = idx
        return [-1,-1]
 
# time complexity: O(n)
# space complexity: O(U)
nums = [3,4,5,6]
target = 7
print(Solution().twoSum(nums, target))   
nums = [5,5]
target = 10
print(Solution().twoSum(nums, target))
nums = [4,5,6]
target = 10
target = 10
print(Solution().twoSum(nums, target))
