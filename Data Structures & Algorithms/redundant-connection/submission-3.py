class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) 

        parents = [i for i in range(0,n+1)] # O(V)
        ranks = [1] * (n+1) # O(V)


        def find(x): # O(α(V))
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]


        def union(a,b):

            parantA = find(a)
            parantB = find(b)

            if parantA == parantB:
                return False
            
            if ranks[parantA] > ranks[parantB]:
                parents[parantB] = parantA
            elif ranks[parantA] < ranks[parantB]:
                parents[parantA] = parantB
            else:
                parents[parantB] = parantA
                ranks[parantA] += 1
            return True

        for a,b in edges: # O(E)
            if not union(a,b):
                return [a,b]
        return []

# time complexity: O(E α(V)+ V)
# space complexity: O(V)
# α is known is ancker man; it's almost constant because the when we run it for afew time most of the elemnts represents the correct parent and we do not need that much resursion every time

        