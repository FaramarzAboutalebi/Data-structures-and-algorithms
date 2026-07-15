# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # time complexity: O(m * n)
        # space complexity: O(h1 + h2)
            # h-> best case: log n, worst case: n
        if not root and not subRoot:
            return True
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTrees(root,subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def sameTrees(self, p: Optional[TreeNode],q:Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return (self.sameTrees(p.left,q.left) and self.sameTrees(p.right,q.right))


        