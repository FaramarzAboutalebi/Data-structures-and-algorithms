class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

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
                return False
            
            if rank[rootA] > rank[rootB]:
                parents[rootB] = rootA
            elif rank[rootB] > rank[rootA]:
                parents[rootA] = rootB
            else:
                parents[rootB] = rootA
                rank[rootA] += 1
            
            return True

        
        components = n

        for a,b in edges:
            if union(a,b):
                components -= 1
        
        return components

# time complexity: O(V + E alpha(V))
# space complexity: O(V)