from typing import List,Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
#         10
#     /           \
# 2                   7
#             /           \
#         5                   8

# preorder = [10,2,7,5,8]
# inorder = [2,10,5,7,8]

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int])->Optional[TreeNode]:
        
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
#time complexity: O(n ^ 2)
#space complexity: O(n ^ 2)