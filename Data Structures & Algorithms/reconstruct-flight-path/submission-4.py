class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        

        adj = defaultdict(list)

        for src,dis in sorted(tickets, reverse=True): # T: O(E logE)
            adj[src].append(dis)

        res = []

        def dfs(airport):
            while adj[airport]:
                nei = adj[airport].pop()
                dfs(nei)
            res.append(airport)

        dfs("JFK")

        res.reverse()

        return res

# T: O(E logE)
# S: O(V + E)