from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self,root: Optional[TreeNode])->bool:
        
        def dfs(cur,leftR,rightR):
            if not cur:
                return True
            if not(leftR < cur.val <rightR):
                return False
            return dfs(cur.left, leftR, cur.val) and dfs(cur.right, cur.val,rightR)
        return dfs(root, float("-inf"),float("inf"))
# time complexity: O(n)
# space complexity: O(h)

root = TreeNode(2,TreeNode(1),TreeNode(3))
print(Solution().isValidBST(root))

# root = [1,2,3]
root = TreeNode(1,TreeNode(2),TreeNode(3))
print(Solution().isValidBST(root))