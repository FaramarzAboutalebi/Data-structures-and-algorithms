

class Solution:
    def uniquePaths(self, m: int, n: int)->int:

        if n == 1 and m == 1:
            return 1
        
        # m : ROWS
        # n: COLS
        dp = [1] * n
        dp[-1] = 0
        
        for r in range(m-1):
            new_dp = [1] * n
            for c in range(n-2,-1,-1):
                new_dp[c] = new_dp[c+1] + dp[c]
            dp = new_dp
            
        return dp[0]

# time complexity: O(n.m)
# space complexity: O(n) 

m = 3
n = 6
print(Solution().uniquePaths(m,n))

m = 3
n = 3
print(Solution().uniquePaths(m,n))
                
            