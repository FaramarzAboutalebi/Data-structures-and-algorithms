from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def maxPathSum(self, root: Optional[TreeNode])->int:
        
        self.res = float("-inf")
        
        def dfs(cur):
            if not cur:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)
            leftMax = max(left,0)
            rigthMax = max(right,0)
            
            self.res = max(self.res, cur.val + leftMax + rigthMax)
            return cur.val + max(leftMax,rigthMax)
        dfs(root)
        return self.res
        
# time complexity: O(n)
# space complexity: O(h)

n1 = TreeNode(-15)
n2 = TreeNode(10)
n3 = TreeNode(20)
n1.left = n2
n1.right = n3
n2.left = None
n2.right = None
n4 = TreeNode(15)
n5 = TreeNode(5)
n3.left = n4
n3.right = n5
n6 = TreeNode(-5)
n4.left = n6
root = n1


print(Solution().maxPathSum(root))
        

            
            
            