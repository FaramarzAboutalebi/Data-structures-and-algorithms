class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parents = list(range(n))
        rank = [1] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(a,b):

            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return 0

            if rank[rootA] > rank[rootB]:
                parents[rootB] = rootA

            elif rank[rootA] < rank[rootB]:
                parents[rootA] = rootB

            else:
                parents[rootB] = rootA
                rank[rootA]
            return 1
        
        components = n

        for a,b in edges:
            components -= union(a,b)
        return components

        

