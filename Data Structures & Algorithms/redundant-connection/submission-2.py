class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        ranks = [1] * (len(edges)+1)
        parents = [i for i in range(len(edges)+1)]

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

# time complexity: O(E α(V) + V)
# space complexity: O(V)