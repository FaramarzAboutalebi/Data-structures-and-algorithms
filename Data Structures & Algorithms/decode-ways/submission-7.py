class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1,len(s)):

            if '1' <= s[i] <= '9':
                dp[i+1] += dp[i]
            
            two_didgit = s[i-1:i+1]
            if "10" <= two_didgit <= "26":
                dp[i+1] += dp[i-1]
        return dp[len(s)]


        