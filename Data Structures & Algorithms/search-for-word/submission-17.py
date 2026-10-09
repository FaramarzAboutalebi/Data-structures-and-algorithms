class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS,COLS = len(board),len(board[0])

        visit = set()

        def dfs(r,c,i):
            if (r,c) in visit:
                return False
            if board[r][c] != word[i]:
                return False
            if i == len(word)-1 and board[r][c] == word[i]:
                return True
            visit.add((r,c))
            for dr,dc in ((1,0),(-1,0),(0,-1),(0,1)):
                nr,nc = r+dr,c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if dfs(nr,nc,i+1):
                        visit.remove((r,c))
                        return True
            visit.remove((r,c))
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True

        return False

# time complexity