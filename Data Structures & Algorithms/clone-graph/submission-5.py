"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        oldToNew = {}

        def dfs(node): # T: O(V), S: O(V)

            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val) # S: O(V)

            oldToNew[node] = copy # S: O(V)

            for nei in node.neighbors: # T: O(E), S: O(E)
                copy.neighbors.append(dfs(nei)) 
            
            return copy
             
        return dfs(node) 

# time complexity: O(V + E)
# space complexity: O(V+E)