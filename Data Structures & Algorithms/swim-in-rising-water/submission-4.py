import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        minHeap = [(grid[0][0],0,0)] # t,r,c
        visit = {(0,0)}
        n = len(grid)
        res = 0

        while minHeap:
            
            t,r,c = heapq.heappop(minHeap)

            res = max(res,t)

            if r == n-1 and c == n-1:
                return res
            
            

            for dr,dc in ((0,-1),(0,1),(-1,0),(1,0)):
                nr,nc = dr+r,dc+c

                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visit:
                    visit.add((nr,nc))
                    heapq.heappush(minHeap, (grid[nr][nc],nr,nc))
        return res


# time complexity: O(N^2 log N)
# space complexity: O(N^2)
        