from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode],q: Optional[TreeNode])->bool:
        
        # time complexity: O(n)
        # space complexity: O(h); best case: O(logn), worst case: O(n)
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left,n1.right = n2,n3

n1_C = TreeNode(1)
n2_C = TreeNode(2)
n3_C = TreeNode(3)
n1_C.left,n1_C.right = n2_C,n3_C

sol = Solution()
res = sol.isSameTree(n1,n1_C)
print(res)