class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        component = n
        parents = [i for i in range(n)]
        ranks = [1] * (n)

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
            elif ranks[parentB] > ranks[parentA]:
                parents[parentA] = parentB
            else:
                parents[parentB] = parentA
                ranks[parentA] += 1
            
            return True

        for a,b in edges:
            if union(a,b):
                component -= 1
        return component
