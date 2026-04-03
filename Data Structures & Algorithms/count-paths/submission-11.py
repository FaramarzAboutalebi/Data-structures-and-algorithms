class Solution:
    def uniquePaths(self, m: int, n: int)->int:
        
        dp = [1] * n
        
        for i in range(m-1):
            new_dp = [1] * n
            for j in range(n-2,-1,-1):
                new_dp[j] = new_dp[j+1] + dp[j]
            dp = new_dp
        return dp[0]

# time complexity: O(n*m)
# space complexity: O(n)

sol = Solution()
print(sol.uniquePaths(3,3))