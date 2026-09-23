from typing import Optional

class TreeNode:
  def __init__(self,val=0,left=None,right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int)->int:

    # time complexity: balanced: O(h+k), worst case: O(n)
    # space complexity: 
      # for stack O(h)-> balanced: O(log n), worst case: O(n)

    stack = []
    cur = root
    
    while cur or stack:
      while cur:
        stack.append(cur)
        cur = cur.left

      node = stack.pop()
      k -= 1
      if k == 0:
        return node.val
        
      cur = node.right

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(7)

sol = Solution()

print(sol.kthSmallest(root,2))
assert sol.kthSmallest(root,2) == 3