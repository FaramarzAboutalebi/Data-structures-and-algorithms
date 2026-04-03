from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int])->int:
        
        if len(nums) == 0:
            return 0
            
        numsSet = set()
        
        for n in nums:
            numsSet.add(n)
        
        res = 1
        
        for n in numsSet:
            if (n-1) not in numsSet:
                counter = 0 
                while n in numsSet:
                    counter += 1
                    n += 1
                res = max(res, counter)
        return res
# time complexity: O(n)
# space complexity: O(n)
nums = [0,3,2,5,4,6,1,1]
print(Solution().longestConsecutive(nums))                
            