class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        res = 0
        visit = set()

        def dfs(i):
            visit.add(i)
            for nei in adj[i]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)


        for i in range(n):
            if i not in visit:
                res += 1
                dfs(i)
        return res