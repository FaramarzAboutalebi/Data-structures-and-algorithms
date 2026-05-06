class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # n = 3
        # [[0,1],[0,2]]
        if n-1 != len(edges):
            return False 
        parents = list(range(n))
        rank = [1] * n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(a,b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False # cycle
             
            if rank[rootA] > rank[rootB]:
                parents[rootB] = rootA
            elif rank[rootB] > rank[rootA]:
                parents[rootA] = rootB
            else:
                parents[rootB] = rootA
                rank[rootA] += 1
            return True

        for a,b in edges:
            if not union(a,b):
                return False
        return True

# time complexity: O(E α(V))
# space complexity: O(V)
