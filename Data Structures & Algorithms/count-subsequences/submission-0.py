class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cash = {}
        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in cash:
                return cash[(i,j)]
            if s[i] == t[j]:
                cash[(i,j)] = dfs(i+1,j+1) + dfs(i+1,j)
            else:
                cash[(i,j)] = dfs(i+1,j) 
            return cash[(i,j)]
        return dfs(0,0)


        