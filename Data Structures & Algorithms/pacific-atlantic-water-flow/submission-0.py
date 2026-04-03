class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific_q, atlantic_q = deque(), deque()
        pacific_visit, atlantic_visit = set(), set()
        ROWS,COLS = len(heights),len(heights[0])

        for r in range(ROWS):
            pacific_q.append((r,0))
            atlantic_q.append((r,COLS-1))
        for c in range(COLS):
            pacific_q.append((0,c))
            atlantic_q.append((ROWS-1,c))
        
        def bfs(q,visit):
            while q:
                r,c = q.popleft()
                visit.add((r,c))
                for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                    nr,nc = r+dr,c+dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visit):
                        q.append((nr,nc))
        
        bfs(pacific_q,pacific_visit)
        bfs(atlantic_q,atlantic_visit)

        return list(pacific_visit & atlantic_visit)

