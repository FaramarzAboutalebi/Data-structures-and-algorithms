from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
   

class Solution:
    def maxDepth(self, root: Optional[TreeNode])->int:
        
        def dfs(cur):
            if not cur:
                return 0
            left = dfs(cur.left)
            right = dfs(cur.right)
            return 1 + max(left,right)
        return dfs(root)
# time complexity: O(n)
# space complexity: O(1)
root = TreeNode(1,TreeNode(2,None,None),TreeNode(3,TreeNode(4),None))
print(Solution().maxDepth(root)) 
root = None
print(Solution().maxDepth(root))
