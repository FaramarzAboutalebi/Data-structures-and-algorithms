from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self,root: Optional[TreeNode])->List[List[int]]:
        
        if not root:
            return []
            
        q = deque([root])
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                
                
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level:
                res.append(level)
        return res
        
# time complexity: O(n)
# space complexity: O(n) output
#root = [1,2,3,4,5,6,7]
root = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
print(Solution().levelOrder(root))

                    
                
        
        