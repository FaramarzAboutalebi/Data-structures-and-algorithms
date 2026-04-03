class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        dp = {}
        dp[0] = 1
        

        for i in range(len(s)):
            dp[i+1] = 0

            if s[i] != '0':
                dp[i+1] = dp[i]
            if i > 0:
                two_digit = s[i-1:i+1]
                if "10" <= two_digit <= "26":
                    dp[i+1] += dp[i-1]
        return dp[len(s)]
        