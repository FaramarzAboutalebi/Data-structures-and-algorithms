from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]])->bool:
        if n -1 != len(edges):
            return False
        
        parents = [i for i in range(n)]
        
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
            
        def union(a,b):
            rootA = find(a)
            rootB = find(b)
            
            if rootA == rootB:
                return False
                
            parents[rootB] = rootA
            return True
        
        for a,b in edges:
            if not union(a,b):
                return False
        return True
# time complexity: O(E α(V)+ V)
# space complexity: O(V)
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(Solution().validTree(n,edges))
            
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print(Solution().validTree(n,edges))
            