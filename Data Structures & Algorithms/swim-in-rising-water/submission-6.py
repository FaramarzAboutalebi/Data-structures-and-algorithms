class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
            
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()

        minheaq = [(grid[0][0],0,0)]
        res = 0

        while minheaq:
            t,r,c = heapq.heappop(minheaq)

            if (r,c) in visit:
                continue
            
            res = max(res, grid[r][c])

            if r == ROWS-1 and c == COLS-1:
                return res

            visit.add((r,c))

            for dr,dc in ((0,-1),(0,1),(-1,0),(1,0)):
                nr,nc = r+dr,c+dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr,nc) not in visit:
                    heapq.heappush(minheaq, (grid[nr][nc],nr,nc))
        return res

# time complexity: O(RC log(RC)) = O(N^2 log N)
# space complexity: O(RC) = O(N^2)
