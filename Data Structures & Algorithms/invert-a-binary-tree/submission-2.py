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
        # space complexity: O(h) -> log n to n
        def dfs(cur):
            if not cur:
                return None
            cur.left,cur.right = cur.right,cur.left
            dfs(cur.left)
            dfs(cur.right)
            return cur
        return dfs(root)
    def printTree(self, root: Optional[TreeNode])->None:
        
        q = deque([root])
        res = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(node.val)

                if node:
                    q.append(node.left)
                    q.append(node.right)

        print(res)
                


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
#root = [.    1
    #     2         3
    #   4  5.     6  7]

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
root = n1
sol = Solution()
root = sol.invertTree(root)
sol.printTree(root)

