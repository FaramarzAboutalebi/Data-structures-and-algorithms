# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

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

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        # time complexity: O(n)
        # space complexity: O(n)
        myData = data.split(",")
        self.i = 0

        def dfs():
            if myData[self.i] == "N":
                self.i += 1
                return None
            
            root = TreeNode(int(myData[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()



