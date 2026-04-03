
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # bottom-up dp
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for a in range(1,amount + 1):
                if a - coin >= 0:
                    dp[a] += dp[a - coin]
        return dp[-1] if dp[-1] != 0 else 0
    
'''
Example 1:

Input: coins = [1,5,10], amount = 12

Output: 3
Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

Example 2:

Input: coins = [2], amount = 3

Output: -1
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:

Input: coins = [1], amount = 0

Output: 0
'''
sol = Solution()

coins = [1,5,10] 
amount = 12
res = sol.change(amount,coins)
print(res)

coins = [2]
amount = 3
res = sol.change(amount,coins)
print(res)

coins = [1]
amount = 0
res = sol.change(amount,coins)
print(res)
# time complexity: O(n * a)
# space complexity: O(a) for dp