class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        board = [["."] * n for i in range(n)]
       
        cols = set()
        negPosition = set()
        posPosition = set()

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if (0 <= c < n and c not in cols and (r-c) not in negPosition and (r+c) not in posPosition):
                    cols.add(c)
                    negPosition.add(r-c)
                    posPosition.add(r+c)
                    board[r][c] = "Q"
                    dfs(r+1)
                    cols.remove(c)
                    negPosition.remove(r-c)
                    posPosition.remove(r+c)
                    board[r][c] = "."
        dfs(0)
        return res