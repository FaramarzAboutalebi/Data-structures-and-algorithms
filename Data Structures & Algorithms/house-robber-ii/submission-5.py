from typing import List

class Solution:
    def rob(self, nums: List[int]):
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]),self.helper(nums[1:]))
    
    def helper(self,numsSub: List[int])->int:
        rob1 = 0
        rob2 = 0
        
        for n in numsSub:
            temp = rob2
            rob2 = max(rob2,rob1+n)
            rob1 = temp
        return rob2
sol = Solution()
nums = [2,9,8,3,6]
print(sol.rob(nums))

# time complexity: O(n)
# space complexity: O(1)