from typing import List

class Solution:
  def validTree(self, n: int, edges: List[List[int]])->bool:

    if n-1 != len(edges):
      return False
      
    parents = [i for i in range(n)]
    ranks = [1] * n

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
        return False

    return True

# time complexity: O(E α(V)+ V)
# space complexity: O(V)