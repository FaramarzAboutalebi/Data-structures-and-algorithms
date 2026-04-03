from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode])->Optional[TreeNode]:
        
        cur = root 
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
# time complexity: O(h)
# space complexity:   O(1)            
# root = [5,3,8,1,4,7,9,null,2]
root = TreeNode(5,TreeNode(3,TreeNode(1),TreeNode(4,None,TreeNode(2))),TreeNode(8,TreeNode(7),TreeNode(9)))
p = root.left
q =  root.right
print(Solution().lowestCommonAncestor(root,p,q).val)
                