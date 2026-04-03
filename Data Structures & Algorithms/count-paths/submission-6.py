class Solution:
    def uniquePaths(self, m: int, n: int)->int:
        # m : rows
        # n: cols
        dp = [1] * n
        
        for _ in range(m-1):
            new_dp = [1] * n
            
            for i in range(n-2,-1,-1):
                new_dp[i] = dp[i] + new_dp[i+1]
            dp = new_dp
        return dp[0]
# time complexity: O(m * n)
# space complexity: O(n)
sol = Solution()
m = 3
n = 6
print(sol.uniquePaths(m,n))