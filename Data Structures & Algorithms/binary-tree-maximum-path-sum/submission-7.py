from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def maxPathSum(self, root:Optional[TreeNode])->int:

    self.res = float("-inf")
    
    def dfs(cur):
        if not cur:
            return 0
    
        left = dfs(cur.left)
        right = dfs(cur.right)

        maxLeft,maxRight = max(left,0),max(right,0)

        self.res = max(self.res, maxLeft + maxRight + cur.val)

        return max(maxLeft + cur.val, maxRight + cur.val)
    dfs(root)
    return self.res