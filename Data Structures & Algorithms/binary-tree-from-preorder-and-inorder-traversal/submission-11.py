# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        self.preIndex = 0
        inorderToIdx = {val:i for i,val in enumerate(inorder)}

        def dfs(left,right):
            if left > right:
                return None

            rootVal = preorder[self.preIndex]
            self.preIndex += 1
            root = TreeNode(rootVal)

            m = inorderToIdx[rootVal]

            root.left = dfs(left,m-1)
            root.right = dfs(m+1,right)

            return root
        
        return dfs(0, len(inorder)-1)

# time complexity: O(n)
# space complexity: O(n)
    # O(n) for nodes
    # O(h) for stack call
