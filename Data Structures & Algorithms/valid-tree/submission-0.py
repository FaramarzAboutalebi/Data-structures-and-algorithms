class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n-1:
            return False

        parent = [i for i in range(n)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True
        
        for a,b in edges:
            if not union(a,b):
                return False
        return True