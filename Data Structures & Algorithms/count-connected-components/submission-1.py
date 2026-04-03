class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1] * n
        parent = [i for i in range(n)]

        components = n  

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rootX,rootY = find(x),find(y)
            if rootX == rootY:
                return False
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
                rank[rootY] += 1
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True


        
        for a,b in edges:
            if union(a,b):
                components -= 1
        return components
