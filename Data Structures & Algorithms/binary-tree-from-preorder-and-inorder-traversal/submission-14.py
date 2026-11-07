# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        self.preorderIdx = 0
        l,r = 0,len(inorder)-1
        inorderToIdx = {val:idx for idx,val in enumerate(inorder)}

        def dfs(l,r):
            if l > r:
                return None
            
            rootVal = preorder[self.preorderIdx]
            root = TreeNode(rootVal)
            mid = inorderToIdx[rootVal]
            self.preorderIdx += 1

            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)

            return root
        return dfs(l,r)

# time complexity: O(n)
# space complexity: O(n)
    # O(n) for nodes
    # O(h) for stack call