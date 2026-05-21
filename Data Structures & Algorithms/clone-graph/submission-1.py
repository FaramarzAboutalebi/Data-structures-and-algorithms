from typing import List, Optional

class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []
class Solution:
    def cloneGraph(self, head: Optional[Node])->Optional[Node]:
        
        if not head:
            return None

        newToCopy = {}

        def dfs(node):
            if node in newToCopy:
                return newToCopy[node]
            
            copy = Node(node.val)

            newToCopy[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
        
        return dfs(head)

# time complexity: O(n)
# space complexity: O(n)
