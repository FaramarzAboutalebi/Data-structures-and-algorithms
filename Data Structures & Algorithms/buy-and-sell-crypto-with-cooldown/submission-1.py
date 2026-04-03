class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def dfs(i,Buying):
            if i >= len(prices): return 0

            cooldown = dfs(i+1,Buying)
            if Buying:
                buy = dfs(i+1,not Buying)
                return max(cooldown, buy - prices[i])
            else:
                sell = dfs(i+2,not Buying)
                return max(sell + prices[i],cooldown)
        return dfs(0, True)
        

        