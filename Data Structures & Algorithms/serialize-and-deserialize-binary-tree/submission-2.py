from typing import Optional

class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Codec:
    def serialize(self, root: Optional[TreeNode])->str:
        # time complexity: O(n)
        # space complexity: O(n)
        res = []
        
        def dfs(cur):
            if not cur:
                res.append("N")
                return 
            res.append(str(cur.val))
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        return ",".join(res)
        
    def deserialize(self, s: str)->Optional[TreeNode]:
         # time complexity: O(n)
        # space complexity: O(n)       
        data = s.split(",")
        self.i = 0
        def dfs():
            
            if data[self.i] == "N":
                self.i += 1
                return None
            root = TreeNode(int(data[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            
            return root
        
        return dfs()
root = TreeNode(1,
        TreeNode(2),
        TreeNode(3, TreeNode(4), TreeNode(5)))

codec = Codec()
s = codec.serialize(root)
print(f"serialized {s}")
root = codec.deserialize(s)
s = codec.serialize(root)
print(f"re serialized {s}")



        