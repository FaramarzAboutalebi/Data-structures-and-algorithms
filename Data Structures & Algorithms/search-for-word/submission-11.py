from typing import List

class Solution:
    def exist(self, board: List[List[int]], word: str)->bool:
        
        ROWS,COLS = len(board), len(board[0])
        
        def dfs(r,c,i):
            if i >= len(word):
                return True
                
            if (r >= ROWS or r < 0 or c >= COLS or c < 0):
                return False
                
            if (board[r][c] != word[i] or board[r][c] == '#'):
                return False
                
            char = board[r][c] 
            board[r][c]  = '#'
            for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                nr,nc = r+dr,c+dc
                if dfs(nr,nc,i+1):
                    return True
                
            board[r][c]  = char
            return False
                
        for r in range(ROWS):
            for c in range(COLS):
                if word[0] == board[r][c]:
                    if dfs(r,c,0):
                        return True
        return False

# time complexity: O(n*m*3^(l-1))
# space complexity: O(l)

board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "BAT"


print(Solution().exist(board,word))

board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "CAT"
print(Solution().exist(board,word))

