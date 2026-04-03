class Solution:
    def numDecodings(self, s: str)-> int:
        if s[0] == '0':
            return 0
            
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(1,len(s)):
            
            if '1' <= s[i] <= '9':
                dp[i+1] += dp[i]
            
            two_digit = s[i-1:i+1]
            if "10" <= two_digit <= "26":
                dp[i+1] += dp[i-1]
        return dp[-1]
'''
Example 1:

Input: s = "12"

Output: 2

Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "01"

Output: 0
'''
sol =  Solution()

s = "12"
res = sol.numDecodings(s)
print(res == 2)

s = "01"
res = sol.numDecodings(s)
print(res == 0)

# time complexity: O(n)
# space complexity: O(n) for dp
                