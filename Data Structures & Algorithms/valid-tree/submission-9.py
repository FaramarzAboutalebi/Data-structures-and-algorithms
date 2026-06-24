class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # no cycle
        # numOf_V = numOf_E + 1

        if n != len(edges) + 1:
            return False

        parants = [i for i in range(n)]
        ranks = [1] * n

        def find(x):
            if x != parants[x]:
                parants[x] = find(parants[x])
            return parants[x]

        def union(a,b):
            parantA = find(a)
            parantB = find(b)

            if parantA == parantB:
                return False
            
            if ranks[parantA] > ranks[parantB]:
                parants[parantB] = parantA
            elif ranks[parantA] < ranks[parantB]:
                parants[parantA] = parantB
            else:
                parants[parantB] = parantA
                ranks[parantA] += 1
            return True
        

        for a,b in edges:
            if not union(a,b):
                return False
        
        return True



# time complexity: O(V + E * alpha)
# space complexity: O(V)
        