from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
   
class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode])->Optional[TreeNode]:
        
        if not root:
            return None
        
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
# root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

# time complexity: O(log n)
# space complexity: O(1)

n5 = TreeNode(5)
n3 = TreeNode(3)
n8 = TreeNode(8)

n1 = TreeNode(1)
n4 = TreeNode(4)
n7 = TreeNode(7)
n9 = TreeNode(9)
n2 = TreeNode(2)
n5.left = n3
n5.right = n8
n3.left = n1
n3.right = n4
n8.left = n7
n8.right = n9
n1.left = None
n1.right = n2
root = n5

res = Solution().lowestCommonAncestor(root, n3,n8)
if res:
    print(res.val)

        
        