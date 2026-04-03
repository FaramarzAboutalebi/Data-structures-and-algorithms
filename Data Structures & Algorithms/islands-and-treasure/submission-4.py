from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()
        ROW,COLS = len(grid),len(grid[0])
        INF = 2147483647

        for r in range(ROW):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
            
        while q:
            r,c = q.popleft()

            for dr,dc in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr,nc = r+dr,c+dc

                if (0 <= nr < ROW and 0 <= nc < COLS and grid[nr][nc] == INF):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))
                    
        