class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS,COLS = len(board),len(board[0])
        root = TrieNode()
        
        for w in words: # O(T)
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = w
        
        res = []
        
        def dfs(r,c,cur):
            if board[r][c] not in cur.children:
                return 
            
            char = board[r][c]
            nxt = cur.children[char]
            
            if nxt and nxt.word:
                res.append(nxt.word)
                nxt.word = None
                
            board[r][c] = '#'
            
            for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                nr,nc = r+dr,c+dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#'):
                    dfs(nr,nc,nxt)
            board[r][c] = char
            
            if not nxt.children and nxt.word is None:
                del cur.children[char]
            
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root)
        return res
        
                
        