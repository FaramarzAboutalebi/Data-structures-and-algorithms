class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        ROWS,COLS = len(grid),len(grid[0])

        inf = 2**31 - 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            r,c = q.popleft()
            for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                nr,nc = r+dr,c+dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == inf):
                    q.append((nr,nc))
                    grid[nr][nc] = grid[r][c] + 1

