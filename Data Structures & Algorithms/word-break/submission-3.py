from typing import List

class Solution:
    def wordBreak(self,s: str, wordDict: List[str])->bool:
        
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if i+len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
         
                if dp[i]:
                    break
        return dp[0]
# time complexity: O(n*m*L)
# space complexity: O(n)
sol = Solution()
s = "neetcode"
wordDict = ["neet","code"]
print(sol.wordBreak(s,wordDict))