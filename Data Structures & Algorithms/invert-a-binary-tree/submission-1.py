from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def invertTree(self, root: Optional[TreeNode])->Optional[TreeNode]:
        # time complexity: O(n)
        # space complexity: O(h)
        def dfs(cur):
            if not cur:
                return None
            cur.left, cur.right = cur.right,cur.left
            dfs(cur.left)
            dfs(cur.right)
            
            return cur
        return dfs(root)
    def printTree(self,root: Optional[TreeNode]):
        res = []
        cur = root
        q = deque()
        q.append(root)
        while q:
            
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
           
                
        return res
# root = [1,2,3,4,5,6,7]
root = TreeNode(1, TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
root = Solution().invertTree(root)   
print(Solution().printTree(root) == [1,3,2,7,6,5,4])
            