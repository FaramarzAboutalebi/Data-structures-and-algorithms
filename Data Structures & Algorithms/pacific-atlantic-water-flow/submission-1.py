class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS,COLS = len(heights), len(heights[0])

        pacific_q = deque()
        atlantic_q = deque()
        pacific_visit = set()
        atlantic_visit = set()

        for c in range(COLS):
            pacific_q.append([0,c]) # Pacific Ocean
            atlantic_q.append([ROWS-1,c]) # Atlantic Ocean

        for r in range(ROWS):
            pacific_q.append([r,0]) # Pacific Ocean
            atlantic_q.append([r,COLS-1]) # Atlantic Ocean


        def bfs(queue, visit):
            while len(queue) != 0:
                r,c = queue.popleft()

                if (r,c) in visit:
                    continue
                
                visit.add((r,c))

                for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)):
                    nr,nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and heights[r][c] <= heights[nr][nc] and (nr,nc) not in visit:
                        queue.append((nr,nc))
                        

        bfs(pacific_q, pacific_visit)
        bfs(atlantic_q, atlantic_visit)

        return list(pacific_visit & atlantic_visit)
                    


            

# time complexity: O(n * m)
# space complexity: O(n * m)