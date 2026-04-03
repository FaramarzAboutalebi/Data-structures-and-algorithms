from typing import List

class Solution:
    def rob(self, nums: List[int])->int:
        if not nums:
            return 0
            
        if len(nums) == 1:
            return nums[0]

        return max(self.robSubList(nums[:len(nums)-1]),self.robSubList(nums[1:]))
        
    def robSubList(self, numSub: List[int])->int:   
        rob1,rob2 = 0,0
        
        for n in numSub:
            temp = rob2
            rob2 = max(n+rob1, rob2)
            rob1 = temp
        return rob2
# time compleixtt: O(n)
# space compleixtt: O(1)
nums = [2,9,8,3,6]
print(Solution().rob(nums))
nums = [3,4,3]
Solution().rob(nums)
