class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # m: row
        # n: col

        if n == 0 and m == 0:
            return 0

        dp = [0] * n

        dp[-1] = 1

        for r in range(m-1,-1,-1):
            for c in range(n-2,-1,-1):
                dp[c] += dp[c+1]
        return dp[0]

