from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode])->int:
        
        # time complexity: O(n)
        # space complexity: O(h)
        
        self.res = float('-inf')
        
        def dfs(cur):
            
            if not cur:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            
            leftMax, rightMax = max(left,0),max(right,0)
            
            self.res = max(self.res, leftMax + rightMax + cur.val)
            
            return cur.val + max(leftMax, rightMax)
            
        dfs(root)
        return self.res
        
n1 = TreeNode(-10)
n2 = TreeNode(4)
n3 = TreeNode(3)

n1.left = n2
n1.right = n3

sol = Solution()
print(sol.maxPathSum(n1))