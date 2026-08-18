from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS,COLS = len(grid),len(grid[0])

        q = deque()
        fresh = 0
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        

        while q and fresh > 0:
            for i in range(len(q)):

                r,c = q.popleft()

                for dr,dc in [(0,-1),(0,1),(-1,0),(1,0)]:
                    nr,nc = r+dr,c+dc

                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            
            res += 1
        
        return res if fresh == 0 else -1
            
# time complexity: O(n * m)
# space complexity: O(n * m)