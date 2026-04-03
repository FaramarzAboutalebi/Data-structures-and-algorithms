from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int])->Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        m = inorder.index(preorder[0]) # O(n)
        root.left = self.buildTree(preorder[1:m+1],inorder[:m])
        root.right = self.buildTree(preorder[m+1:],inorder[m+1:])
        return root

# time complexity: O(n^n)
# space complexity: O(n)
preorder = [1,2,3,4]
inorder = [2,1,3,4]
root = Solution().buildTree(preorder,inorder)

q = deque([root])
res = []
while q:
    for _ in range(len(q)):
        node = q.popleft()
        if not node:
            res.append("null")
        else:
            res.append(str(node.val))
        if node:
            q.append(node.left)
            q.append(node.right)
print(res)

