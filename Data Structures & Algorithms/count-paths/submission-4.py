class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        # bottom-up dp
        dp = [[0 for j in range(n)]
                for i in range(m)]
        dp[m-1][n-1] = 1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i+1 < m:
                    dp[i][j] += dp[i+1][j]
                if j+1 < n:
                    dp[i][j] += dp[i][j+1]
        return dp[0][0]
        
sol = Solution()
m = 3
n = 6
print(sol.uniquePaths(m,n))
m = 3
n = 3
print(sol.uniquePaths(m,n))
        