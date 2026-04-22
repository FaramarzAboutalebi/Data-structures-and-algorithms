from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str])->List[str]:
        
        Rows,Cols = len(board), len(board[0])
        
        root = TrieNode()

        # time complexity :O(T)
        # space complexity :O(T)
        for word in words:
            temp = root
            for c in word:
                if c not in temp.children:
                    temp.children[c] = TrieNode()
                temp = temp.children[c]
            temp.word= word
            
        visit = set()
        res = []
        
        # space complexity: O(L)
        def dfs(r,c,node):
            
            char = board[r][c]
            cur_node = node.children.get(char)
            
            if not cur_node or (r,c) in visit:
                return 
            
            visit.add((r,c))
            
            if cur_node.word:
                res.append(cur_node.word)
                cur_node.word = None
            for dr,dc in [[0,1],[1,0],[0,-1],[-1,0]]:
                nr,nc = r+dr,c+dc
                if 0 <= nr < Rows and 0 <= nc < Cols and (nr,nc) not in visit:
                    dfs(nr,nc,cur_node)
            
            visit.remove((r,c))
                
            
            
        # time complexity :O(n * m)   
        for r in range(Rows):
            for c in range(Cols):
                dfs(r,c,root)
        
        return res
                
                
                  
 # time complexity: O(T + n * m * 4 * 3^L)
 # space complexity: O(T + L)            