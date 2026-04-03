class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {src:[] for src,dist in tickets}
        res = []
        res.append("JFK")
        for u,v in tickets:
            adj[u].append(v)
        
        def dfs(airpost):
            if len(tickets) + 1 == len(res):
                return True
            if airpost not in adj:
                return False
        
            for i,neiAirpost in enumerate(adj[airpost]):
                adj[airpost].pop(i)
                res.append(neiAirpost)
                if dfs(neiAirpost): return True
                adj[airpost].insert(i,neiAirpost)
                res.pop()

            return False
        

        dfs("JFK")
        return res

