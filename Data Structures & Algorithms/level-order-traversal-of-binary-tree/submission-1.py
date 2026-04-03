from typing import Optional,List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode])->List[List[int]]:
        
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
# space complexity: O(n) for q


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
'''
root = [1,2,3,4,5,6,7]

                1
        2               3 
    4       5       6       7
'''
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

root = n1
print(Solution().levelOrder(root) == [[1],[2,3],[4,5,6,7]])             
            
        
        
        