class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list) #S: O(E+V)

        for src,dst in sorted(tickets, reverse=True): #T: O(E log E)
            adj[src].append(dst)
        
        res = []

        def dfs(airport):

            while adj[airport]:
                nei = adj[airport].pop()
                dfs(nei)
            
            res.append(airport)

        dfs("JFK") # T: (E)
        
        return res[::-1]
# time complexity: O(E log E)
# space complexity: O(E + V)