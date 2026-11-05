from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list) # S: O(V + E)

        for u,v,t in times: # T: O(E)
            adj[u].append((v,t))
        
        minHeap = [(0,k)] # tiem, node  # S: O(E)

        res = 0
        visit = set() # S: O(V)

        # dijkstra
        while minHeap:

            time,node = heapq.heappop(minHeap) # T: O(log n)

            if node in visit:
                continue
            
            visit.add(node)
            res = time

            for nei,weight in adj[node]: # T: O(E)
                if nei not in visit:
                    heapq.heappush(minHeap, (time+weight, nei))  # T: O(log (E+1))
        return res if len(visit) == n else -1

# time complexity: O(V + E log(E+1))
# space complexity: O(V + E)
                    
