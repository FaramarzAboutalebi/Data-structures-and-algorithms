class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1

        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            rootX, rootY = find(x),find(y)

            if rootX == rootY:
                return False
            parent[rootY]  = rootX
            return True

        for a,b in edges:
            if not union(a,b):
                return [a,b]
        return []