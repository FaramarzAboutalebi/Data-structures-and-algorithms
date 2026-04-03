class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = {}
        for i in range(len(points)):
            x1,y1 = points[i]
            for j in range(i+1, len(points)):
                x2,y2 = points[j]
                w = abs(x1-x2) + abs(y1-y2)
                if i not in edges:
                    edges[i] = []
                if j not in edges:
                    edges[j] = []
                edges[i].append([w,j])
                edges[j].append([w,i])
        minHeap = [(0,0)]
        visit = set()
        res = 0
        while len(visit) < len(points):
            cost,point = heapq.heappop(minHeap)
            if point in visit:
                continue
            visit.add(point)
            res += cost

            for neiCost,neiPoint in edges.get(point,[]):
                heapq.heappush(minHeap,(neiCost,neiPoint))
        return res



        