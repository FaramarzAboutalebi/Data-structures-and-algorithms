class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        for u,v,t in times:
            adj[u].append([t,v])
        minHeap = [(0,k)]
        visit = set()
        res = 0
        while minHeap:
            t,v = heapq.heappop(minHeap)
            if v in visit:
                continue
            visit.add(v)
            res = max(res,t)
            for neiT,neiNode in adj[v]:
                heapq.heappush(minHeap, (t+neiT,neiNode))
        return res if len(visit) == n else -1

