# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(cur,maxN):
            if not cur:
                return 
            if cur.val >= maxN:
                self.res += 1
                maxN = cur.val
            dfs(cur.left,maxN)
            dfs(cur.right,maxN)

        
        dfs(root, float("-inf"))
        return self.res

        