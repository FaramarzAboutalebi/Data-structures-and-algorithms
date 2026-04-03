class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        numberOfAirPorts = len(tickets) + 1

        edges = {}

        for u,v in tickets:
            if not u in edges:
                edges[u] = [] # heap
            heapq.heappush(edges[u],v)
        res = []

        def dfs(airport):
            while edges.get(airport):
                next_dest = heapq.heappop(edges[airport])
                dfs(next_dest)
            res.append(airport)

        dfs("JFK")
        res = res[::-1]
        return res


        


        