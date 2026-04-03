
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]])->bool:
        
        if len(edges) != n-1:
            return False
        # find union
        parants = [i for i in range(n)]
        
        def find(x):
            if x != parants[x]:
                parants[x] = find(parants[x])
            return parants[x]
            
        def union(a,b):
            rootA = find(a)
            rootB = find(b)
            
            if rootA == rootB:
                return False
                
            parants[rootB] = rootA
            return True
        
        for a,b in edges:
            if not union(a,b):
                return False
        return True
        
# time complexity:
# space complexity:
sol = Solution()
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(sol.validTree(n,edges))
            
            
            