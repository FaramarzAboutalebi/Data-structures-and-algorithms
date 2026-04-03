from typing import List

class Solution:
    def maxProduct(self, nums: List[int])->int:
        maxP,minP = 1,1
        res = float("-inf")
        for n in nums:
            if n == 0:
                maxP,minP = 1,1
            temp = maxP
            maxP = max(n, n * maxP, n * minP)
            minP = min(n, n * temp, n * minP)
            res = max(res, maxP)
        return res
# time complexity: O(n)
# space compleixy: O(1)
nums = [1,2,-3,4]       
print(Solution().maxProduct(nums))