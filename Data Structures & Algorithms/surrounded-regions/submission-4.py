from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS,COLS = len(board),len(board[0])
        q = deque()

        for r in range(ROWS):
            if board[r][0] == 'O':
                board[r][0] = 'Z'
                q.append((r,0))
            if board[r][COLS-1] == 'O':
                q.append((r,COLS-1))
                board[r][COLS-1] = 'Z'
        for c in range(COLS):
            if board[0][c] == 'O':
                q.append((0,c))
                board[0][c] = 'Z'
            if board[ROWS-1][c] == 'O':
                q.append((ROWS-1,c))
                board[ROWS-1][c] = 'Z'
        
        while q:
            r,c = q.popleft()

            for dr,dc in [(0,-1),(0,1),(-1,0),(1,0)]:
                nr,nc = r+dr,c+dc

                if (0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == 'O'):
                    q.append((nr,nc))
                    board[nr][nc] = 'Z'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'Z':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'


# time complexity: O(n * m)
# space complexity: O(n * m)     