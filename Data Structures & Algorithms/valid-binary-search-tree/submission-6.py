from typing import Optional

class TreeNode:
  def __init__(self,val=0,left=None,right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isValidBST(self, root: Optional[TreeNode])->bool:

    # time complexity: O(n)
    # space complexity: O(h)-> balanced: O(log n), worst case: O(n)
    def dfs(cur, leftRange, rightRange):
      if not cur:
        return True
      if not (leftRange < cur.val < rightRange):
        return False
        
      return dfs(cur.left, leftRange, cur.val) and dfs(cur.right, cur.val, rightRange)

    return dfs(root, float("-inf"),float("inf"))
         #  invalid
         #               5
         # 
         #      3               2
         # 1         4

root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(2)

sol = Solution()
print(sol.isValidBST(root))

      