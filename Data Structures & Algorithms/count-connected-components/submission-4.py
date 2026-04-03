class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        rank = [1 for i in range(n)]
        parent = [i for i in range(n)]

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(a,b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                return False
            if rank[a] > rank[b]:
                parent[rootB] = rootA
            elif rank[a] < rank[b]:
                parent[rootA] = rootB
            else:
                parent[rootB] = rootA
                rank[a] += 1
            return True
            
        components = n
        for a,b in edges:
            
            if union(a,b):
                components -= 1
        return components

        