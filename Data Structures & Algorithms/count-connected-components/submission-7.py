from typing import List

class Solution:
    def countComponents(self, n:int, edges: List[List[int]])->int:
        
        parants = [i for i in range(n)]
        rank = [1] * n
        
        def find(x):
            if x != parants[x]:
                parants[x] = find(parants[x])
            return parants[x]
        
        def union(a,b)->bool:
            rootA = find(a)
            rootB = find(b)
            
            if rootA == rootB:
                return False
            if rank[rootA] < rank[rootB]:
                parants[rootA] = rootB
            elif rank[rootA] > rank[rootB]:
                parants[rootB] = rootA
            else:
                parants[rootB] = rootA
                rank[rootA] += 1
            return True
        
        components = n
        
        for a,b in edges:
            if union(a,b):
                components -= 1
        return components
# time comlexity: O(E ⍺(V) +V)
# space complexity: O(V)
n=3
edges=[[0,1], [0,2]]
print(Solution().countComponents(n,edges))  
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]
print(Solution().countComponents(n,edges))  

                
                
                
                
                
            