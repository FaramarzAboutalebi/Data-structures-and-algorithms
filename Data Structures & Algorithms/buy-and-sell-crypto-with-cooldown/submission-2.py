class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i,Buying):
            if i >= len(prices): return 0
            if (i,Buying) in dp:
                return dp[(i,Buying)]
            cooldown = dfs(i+1,Buying)
            if Buying:
                buy = dfs(i+1,not Buying)
                dp[(i,Buying)] = max(cooldown, buy - prices[i])
            else:
                sell = dfs(i+2,not Buying)
                dp[(i,Buying)] = max(sell + prices[i],cooldown)
            return dp[(i,Buying)]
        return dfs(0, True)
        

        