# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):

        # time complexity: O(n)
        # space complexity: 
            # res: O(n)
            # stack call: O(h)-> best case: O(log n), worst case: O(n)

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
        

    def deserialize(self, data):

        # time complexity: O(n)
        # space complexity: 
            # nodes: O(n)
            # stack call: O(h)-> best case: O(log n), worst case: O(n)

        rawData = data.split(",")
        
        self.i = 0
        
        def dfs():
            
            if rawData[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(rawData[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            
            return node
            
        root = dfs()
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



