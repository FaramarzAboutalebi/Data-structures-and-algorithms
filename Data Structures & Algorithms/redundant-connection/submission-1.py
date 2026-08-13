class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        n = len(edges) 

        parents = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(a,b):
            parentA = find(a)
            parentB = find(b)

            if parentA == parentB:
                return False

            if rank[parentA] > rank[parentB]:
                parents[parentB] = parentA
            elif rank[parentA] < rank[parentB]:
                parents[parentA] = parentB
            else:
                parents[parentB] = parentA
                rank[parentA] += 1
            return True


        
        for a,b in edges:
            if not union(a,b):
                return [a,b]
        return []

# time complexity: O(E α(V)+ V)
# space complexity: O(V)
