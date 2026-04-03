class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        maxArea = 0
        self.area = 0

        def dfs(r,c):
           grid[r][c] = 0 
           self.area += 1

           for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
            nr,nc = r+dr,c+dc
            if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                dfs(nr,nc)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.area = 0
                    dfs(r,c)
                    maxArea = max(maxArea,self.area)
        return maxArea
