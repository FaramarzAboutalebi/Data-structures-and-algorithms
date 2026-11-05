import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        heapMin = [(0,0)]# cost, pont idx
        visit = set()
        res = 0
        

        while len(visit) < len(points):

            cost, i = heapq.heappop(heapMin)

            if i in visit:
                continue
            
            x1,y1 = points[i]
            
            res += cost

            visit.add(i)

            for j in range(len(points)):
                if j not in visit:

                    x2,y2 = points[j]
                    dis = abs(x1-x2) + abs(y1-y2)
                    heapq.heappush(heapMin,(dis,j))
        return res

# Time complexty: O(N^2 log N)
# Space complexty: O(N^2)         
