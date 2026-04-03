class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n != len(edges) + 1:
            return False

        # use union find
        parents = [i for i in range(n)]

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]

        def unin(a,b):
            parent1 = find(a)
            parent2 = find(b) 

            if parent1 == parent2:
                return False
            
            parents[b] = a
            return True
            


        for a,b in edges:
            if not unin(a,b):
                return False
        return True
        