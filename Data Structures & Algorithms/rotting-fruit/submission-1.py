class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS,COLS = len(grid),len(grid[0])
        numOfFresh = 0
        q = deque()
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    numOfFresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while q and numOfFresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                    nr,nc = r+dr,c+dc
                    if(0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        numOfFresh -= 1
                        q.append((nr,nc))
                
            time += 1


        return time if numOfFresh == 0 else -1
