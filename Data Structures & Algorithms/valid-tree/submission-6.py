from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n-1 != len(edges):
            return False
        
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()

        def dfs(i):


            visit.add(i)

            for nei in graph[i]:
                if nei not in visit:
                    dfs(nei)
        dfs(0)
        
        return n == len(visit)

# time complexity: O(E + V)
# space complexity: O(E + V)

        