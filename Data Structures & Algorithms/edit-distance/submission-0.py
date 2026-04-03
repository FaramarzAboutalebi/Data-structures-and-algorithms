class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[float("inf") for i in range(len(word2)+1)]
                for j in range(len(word1)+1)]
        ROWS,COLS = len(word1) + 1,len(word2) + 1

        for r in range(ROWS):
            dp[r][COLS-1] = len(word1) -r
        for c in range(COLS):
            dp[ROWS-1][c] = len(word2) -c

        for r in range(ROWS-2,-1,-1):
            for c in range(COLS-2,-1,-1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r+1][c+1]
                else:
                    dp[r][c] = 1 + min(dp[r][c+1],dp[r+1][c+1],dp[r+1][c])
        return dp[0][0]

