# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(cur, leftRange, rightRange)-> bool:
            if not cur:
                return True
            
            if not (leftRange < cur.val < rightRange):
                return False

            return dfs(cur.left, leftRange, cur.val) and dfs(cur.right, cur.val, rightRange)
        

        return dfs(root, float("-inf"), float("inf"))


# time complexity: O(n)
# space complexity: O(h)
    # balance: O(log n)
    # worst case: O(n)