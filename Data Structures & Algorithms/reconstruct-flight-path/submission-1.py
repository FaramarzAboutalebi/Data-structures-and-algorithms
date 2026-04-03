class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)
        '''
        adj = [
            minheap
            minheap
            minHeap
        ]
        '''
        res = []
        for src,dist in tickets:
            # adj[src].append(dist)
            heapq.heappush(adj[src], dist)
        def dfs(node): #JFK
            while adj[node]:
                new_dist = heapq.heappop(adj[node]) # log(n)
                dfs(new_dist)
            res.append(node)
        dfs("JFK")
        return res[::-1]