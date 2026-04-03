from typing import Optional

class TreeNode:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
  
class Solution:
    def isSubtree(self, root: Optional[TreeNode],subRoot: Optional[TreeNode])->bool:
        
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.areTheyTheSame(root, subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def areTheyTheSame(self, p: Optional[TreeNode],q: Optional[TreeNode])->bool:
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.areTheyTheSame(p.left,q.left) and self.areTheyTheSame(p.right,q.right)
        
# time complexity: O(n)
# space complexity: O(h)-> best case: log n, worst case: n
root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3))

subRoot = TreeNode(2,TreeNode(4),TreeNode(5))
print(Solution().isSubtree(root,subRoot))