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
        oldToCopy = {}

        def dfs(cur):
            if cur in oldToCopy:
                return oldToCopy[cur]

            copy = Node(cur.val)
            oldToCopy[cur] = copy

            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        return dfs(node)


# time complexity: O(V + E)
# space complexity:   O(V)  
    # - hashmap: O(V + E)
    # - stack call: O(V)
    # - output tree: O(V + E)