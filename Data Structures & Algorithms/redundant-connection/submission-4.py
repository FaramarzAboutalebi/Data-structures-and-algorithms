class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges) 

        parents = [i for i in range(n+1)]
        ranks = [1] * (n+1)

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(a,b):

            parentA = find(a)
            parentB = find(b)

            if parentA == parentB:
                return False
            if ranks[parentA] > ranks[parentB]:
                parents[parentB] = parentA
            elif ranks[parentA] < ranks[parentB]:
                parents[parentA] = parentB
            else:
                parents[parentB] = parentA
                ranks[parentA] += 1
            return True

        for a,b in edges:
            if not union(a,b):
                return [a,b]
        return []

# time complexity: O(V + E ⍺(V))
# space complexity: O(V)

# ⍺ is inverse ackermann function that grows very slowly, so it's ractically consider constant. Because of path compression and union by rank, each union find operation takes almost O(1) amortized time.
