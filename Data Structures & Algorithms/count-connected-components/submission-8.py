from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]])->int:
        
        # union find
        parents = [i for i in range(n)]
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
            elif rank[rootA] < rank[rootB]:
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
        
# time complexity: O(V + E ⍺(V))
# space complexity: O(V)

n = 6
edges = [[0,1], [1,2], [2,3], [4,5]]
print(Solution().countComponents(n,edges))
                
                
                
                