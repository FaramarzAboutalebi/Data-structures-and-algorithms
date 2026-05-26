# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # time complexity: O(n)
        # space complexity: O(h) -> best case: O(logn), worst case: O(n)

        self.res = float("-inf")

        def dfs(cur):
            if not cur:
                return 0

            leftVal = dfs(cur.left)
            rightVal = dfs(cur.right)

            maxLeft,maxRight = max(leftVal, 0), max(rightVal,0)

            self.res = max(self.res, cur.val + maxLeft + maxRight)

            return cur.val + max(maxLeft, maxRight)
    
        dfs(root)
        return self.res




        