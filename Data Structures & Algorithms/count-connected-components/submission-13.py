class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parants = [i for i in range(n)]
        rank = [1] * n
        components = n

        def find(x):

            if x != parants[x]:
                parants[x] = find(parants[x])

            return parants[x]

        def union(a,b):
            parantA = find(a)
            parantB = find(b)

            if parantA == parantB:
                return False

            if rank[parantA] > rank[parantB]:
                parants[parantB] = parantA
            elif rank[parantA] < rank[parantB]:
                parants[parantA] = parantB
            else:
                parants[parantB] = parantA
                rank[parantA] += 1
            
            return True

        for a,b in edges:
            if union(a,b):
                components -= 1
        return components


# Time complexity: O(V + alpha * E)
# space complexity: O(V)

