from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k:int)->int:
        
        cur = root
        stack = []
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop() # O(1)
            k -= 1
            
            if k == 0:
                return node.val
            cur = node.right
            
# time complexity: O(h+k)
# space complexity: O(h) for stack
root = TreeNode(2,TreeNode(1),TreeNode(3))
k = 1
print(Solution().kthSmallest(root,k))
# root = [4,3,5,2,null]
k = 4
root = TreeNode(4,TreeNode(3,TreeNode(2),None),TreeNode(5))
print(Solution().kthSmallest(root,k))
            