class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges_t = {}

        for u,v,t in times:
            if u not in edges_t:
                edges_t[u] = []
            edges_t[u].append([t,v])
        minHeap = [(0,k)]
        visit = set()
        while minHeap:
            t,node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            if len(visit) == n:
                return t
            for neiT,neiNode in edges_t.get(node,[]):
                heapq.heappush(minHeap,(neiT+t, neiNode))
        return -1
            