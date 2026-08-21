from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(cur):
            if not cur:
                return None
            
            cur.left, cur.right = cur.right, cur.left
            dfs(cur.left)
            dfs(cur.right)

            return root


        return dfs(root)

# time complexity: O(n)
# space complexity: O(h)
    # balanced: O(log n)
    # worst case: O(n)