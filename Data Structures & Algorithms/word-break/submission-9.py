class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s)+1)
        dp[-1] = True

        for i in range(len(s)-1,-1,-1):

            for word in wordDict:
                if i + len(word) < len(dp) and s[i:i+len(word)] == word and dp[i + len(word)]:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
                
        return dp[0]

# time complexity: O(n * m)
# space complexity: O(n)
        