from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        pacific_q, atlantic_q = deque(),deque()
        pacific_visit, atlantic_visit = set(),set()
        ROWS,COLS = len(heights),len(heights[0])

        for r in range(ROWS):
            pacific_q.append((r,0)) # Pacific
            atlantic_q.append((r,COLS-1)) # Atlantic
        for c in range(COLS):
            pacific_q.append((0,c)) # Pacific
            atlantic_q.append((ROWS-1,c)) # Atlantic

        
        def bfs(q,visit):

            while q:
                r,c = q.popleft()

                if (r,c) in visit:
                    continue
                
                visit.add((r,c))

                for dr,dc in ((0,-1),(0,1),(-1,0),(1,0)):
                    nr,nc = r+dr,c+dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and heights[r][c] <= heights[nr][nc]:
                        q.append((nr,nc))
                      
        
        bfs(pacific_q,pacific_visit)
        bfs(atlantic_q,atlantic_visit)


        return list(pacific_visit & atlantic_visit)


# time complexity: O(n * m)
# space complexity: O(n * m)