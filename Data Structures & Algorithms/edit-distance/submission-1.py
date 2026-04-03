class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        cash = [[float("inf") for i in range(len(word2)+1)]
                for j in range(len(word1)+1)]
        
        for j in range(len(word2)+1):
            cash[len(word1)][j] = len(word2) - j
        for i in range(len(word1)+1):
            cash[i][len(word2)]  = len(word1) - i

        for i in range(len(word1)-1, -1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    cash[i][j]  = cash[i+1][j+1]
                else:
                    cash[i][j]  = 1 + min(cash[i+1][j+1] ,cash[i+1][j] ,cash[i][j+1])
            
        return cash[0][0]


        