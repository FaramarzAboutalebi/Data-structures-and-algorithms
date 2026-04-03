class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()
        minHeap = [(grid[0][0],0,0)]
        res = 0
        while minHeap:
            t,r,c = heapq.heappop(minHeap)
            if (r,c) in visit:
                continue
            res = max(t,res)
            visit.add((r,c))
            if r == ROWS-1 and c == COLS-1:
                return res

            for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                nr,nc = r+dr,c+dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visit):
                    heapq.heappush(minHeap, (grid[nr][nc],nr,nc))
            

        