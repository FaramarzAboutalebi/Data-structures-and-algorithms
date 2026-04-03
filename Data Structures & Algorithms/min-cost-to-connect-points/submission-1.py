class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # using Djikstra
        adj = {i:[] for i in range(len(points))}
        for i in range(len(points)):
            x1,y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2,y2 = points[j][0], points[j][1]

                dist = abs(x1 - x2) + abs(y1 - y2) #|xi - xj| + |yi - yj|
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        minHeap = [(0,0)]
        cost = 0
        visit = set()
        while minHeap:
            dist, point = heapq.heappop(minHeap)
            if point in visit:
                continue
            visit.add(point)
            cost += dist
            for distNie, pointNie in adj[point]:
                heapq.heappush(minHeap, (distNie, pointNie))
        return cost

