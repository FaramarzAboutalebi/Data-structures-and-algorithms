from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        freshNum = 0
        q = deque()
        ROWS,COLS = len(grid),len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshNum += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        time = 0

        while q and freshNum > 0:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        freshNum -= 1
                        q.append((nr,nc))
            time += 1


        
        return time if freshNum == 0 else -1

# time complexity: O(n * m)
# space complexity:O(n * m)
