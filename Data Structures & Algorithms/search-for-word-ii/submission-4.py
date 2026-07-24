class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        ROWS,COLS = len(board),len(board[0])
        trie = TrieNode()

        for word in words:
            cur = trie
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = word
        
        visit = set()
        res = []

        def dfs(r,c,node):
            char = board[r][c]

            cur_node = node.children.get(char)

            if not cur_node or (r,c) in visit:
                return 
            
            if cur_node.word:
                res.append(cur_node.word)
                cur_node.word = None

            visit.add((r,c))

            for dr,dc in ((0,-1),(-1,0),(0,1),(1,0)):
                nr,nc = r+dr,c + dc

                if (0 <= nr < ROWS and 0 <= nc < COLS):
                    dfs(nr,nc, cur_node)
            
            visit.remove((r,c))




        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,trie)

        return res

# time complexity: O(T + m * n * 4 * 3^l)
# space complexity: O(T + L)
        
