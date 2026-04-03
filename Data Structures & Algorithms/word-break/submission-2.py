from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom-up dp
        dp = [False] * (len(s)+1)
        dp[-1] = True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]

# time complexity: O(n)
# space complexity: O(1)

sol = Solution()
s = "neetcode"
wordDict = ["neet","code"]
print(sol.wordBreak(s,wordDict))

s = "applepenapple"
wordDict = ["apple","pen","ape"]
print(sol.wordBreak(s,wordDict))

s = "catsincars"
wordDict = ["cats","cat","sin","in","car"]
print(sol.wordBreak(s,wordDict))