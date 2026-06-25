class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = TrieNode()
        ROWS,COLS = len(board),len(board[0])
         
        for word in words:
            cur = trie

            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isWord = word
        
        res = []
        visit = set()

        def dfs(r,c, node):
            
            char = board[r][c]
            cur_node = node.children.get(char)

            if not cur_node or (r,c) in visit:
                return 

            visit.add((r,c))

            if cur_node.isWord:
                res.append(cur_node.isWord)
                cur_node.isWord = None

            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr,nc = r+dr, c+dc
                if (0 <= nr < ROWS and 0 <= nc < COLS):
                    dfs(nr,nc, cur_node)
            visit.remove((r,c))


            


        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, trie)

        return res

# timr complexity: O(T + n * m * 4 * 3^L)
# space complexity: O(T + L)
        