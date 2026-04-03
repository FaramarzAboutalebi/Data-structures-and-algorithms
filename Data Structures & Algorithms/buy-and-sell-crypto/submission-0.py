from typing import List

class Solution:
    def maxProfit(self, prices: List[int])->int:
        
        l = 0
        res = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            res = max(res, prices[r]-prices[l])
        return res
# time complexity: O(n)
# space complexity: O(1)
prices = [10,1,5,6,7,1] 
print(Solution().maxProfit(prices))