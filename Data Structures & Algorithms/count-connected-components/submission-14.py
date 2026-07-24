class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # find union


        parent = [i for i in range(n)]
        rank = [1] * n
        components = n

        def find(x):

            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            parentA = find(a)
            parentB = find(b)
            
            if parentA == parentB:
                return False
            if rank[parentA] > rank[parentB]:
                parent[parentB] = parentA
            elif rank[parentA] < rank[parentB]:
                parent[parentA] = parentB
            else:
                parent[parentB] = parentA
                rank[parentA] += 1
            return True 

        for a,b in edges:
            if union(a,b):
                components -= 1
        
        return components

# time complexity: O(E + V α(E))
# space complexity: O(V)


