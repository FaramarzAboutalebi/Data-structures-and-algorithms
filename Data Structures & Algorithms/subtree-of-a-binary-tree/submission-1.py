from typing import Optional

class NodeTree:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[NodeTree], subarray: Optional[NodeTree])->bool:
        # time complexity: O(n.m)
        # space complexity: O(h)->O(log(min(n,m))) to O(min(n,m))
        if not subarray:
            return True
        if not root:
            return False
        if self.areTheyTheSame(root,subarray):
            return True
        return self.isSubtree(root.left,subarray) or self.isSubtree(root.right,subarray)
    
    def areTheyTheSame(self, p: Optional[NodeTree], q: Optional[NodeTree])->bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.areTheyTheSame(p.left,q.left) and self.areTheyTheSame(p.right,q.right)
        
# root = [  1
#         2  3
#       4 5], 

n1 = NodeTree(1)
n2 = NodeTree(2)
n3 = NodeTree(3)
n4 = NodeTree(4)
n5 = NodeTree(5)
n1.left = n2
n2.right = n3
n2.left = n4
n2.right = n5
root = n1

# subRoot = [2,4,5]
node2 = NodeTree(2)
node4 = NodeTree(4)
node5 = NodeTree(5)
node2.left = node4
node2.right = node5
subRoot = node2

print(Solution().isSubtree(root,subRoot))