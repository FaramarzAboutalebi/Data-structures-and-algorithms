class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = TrieNode()
        ROWS,COLS = len(board),len(board[0])


        for w in words:
            temp = trie
            for c in w:
                if c not in temp.children:
                    temp.children[c] = TrieNode()
                
                temp = temp.children[c]
            temp.isWord = w

        visit = set()
        res = []

        def dfs(r,c,node):

            char = board[r][c]
            cur_node = node.children.get(char)

            if not cur_node or (r,c) in visit:
                return 
            
            visit.add((r,c))

            if cur_node.isWord:
                res.append(cur_node.isWord)
                cur_node.isWord = None


            for dr,dc in ((0,1),(1,0),(-1,0),(0,-1)):
                nr,nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    dfs(nr,nc,cur_node)
            
            visit.remove((r,c))


        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, trie)
        return res


# time complexity: O(T + m * n * 4 * 3 ^ L)
# space complexity: O(T + L)