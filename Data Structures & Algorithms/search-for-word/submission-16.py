class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS,COLS = len(board),len(board[0])

        visit = set()

        def dfs(r,c,i):

            if (r,c) in visit or word[i] != board[r][c]:
                return False

            if i == len(word)-1:
                return True
            
            visit.add((r,c))

            for dr,dc in ((0,-1),(0,1),(-1,0),(1,0)):
                nr,nc = r+dr,c+dc

                if (0 <= nr < ROWS and 0 <= nc < COLS):
                    if dfs(nr,nc, i+1):
                        visit.remove((r,c))
                        return True
            visit.remove((r,c))
            return False
            

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False


# time complexity: O(n * m * 4 * 3^L)
# space complexity: O(L)