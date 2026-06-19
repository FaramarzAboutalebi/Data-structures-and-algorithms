class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for a in range(amount+1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], 1 + dp[a-coin])
        return dp[-1] if dp[-1] != float("inf") else -1
    
# time complexity: O(n * m)
# space complexity: O(n)