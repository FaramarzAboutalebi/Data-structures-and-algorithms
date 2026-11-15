import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list) # S: O(E+V)

        for u,v,t in times: # T: O(E)
            adj[u].append((v,t))
        minheap = [(0,k)] # time, source. # S: O(E+1)

        res = 0

        visit = set()

        while minheap: # T: O(V + E log(E+1))
            time,node = heapq.heappop(minheap)

            if node in visit:
                continue

            visit.add(node)
            res = time

            for nei,weight in adj[node]:
                heapq.heappush(minheap, (time+weight,nei))

        return res if len(visit) == n else -1

# time complexity: O(V + E log(E+1))
# space complexity: O(V+E)     