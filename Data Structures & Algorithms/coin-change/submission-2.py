class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for a in range(amount+1):
                if a - coin >= 0:
                    dp[a] = min(dp[a],dp[a - coin]+1)


        return dp[-1] if dp[-1] != float("inf") else -1
            
        