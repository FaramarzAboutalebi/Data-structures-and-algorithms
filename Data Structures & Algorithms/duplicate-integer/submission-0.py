from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]):
        
        vist = set()
        
        for n in nums:
            if n in vist:
                return True
            vist.add(n)
        return False
# time complexity: O(n)
# space complexity: O(n)
nums = [1, 2, 3, 3]
print(Solution().hasDuplicate(nums))
nums = [1, 2, 3, 4]
print(Solution().hasDuplicate(nums))
