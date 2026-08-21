class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    # time complexity: O(L)
    # space complexity: O(L)
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        

    # time complexity:
        # without '.': O(L)
        # with '.' worst case: O(L^26)
    # space complexity: O(L)    
    def search(self, word: str) -> bool:
        

        def dfs(i,node):

            for j in range(i,len(word)):
                c = word[j]

                if c == '.':
                    for child in node.children.values():
                        if dfs(j+1,child):
                            return True
                    return False

                if c not in node.children:
                    return False
                node = node.children[c]
            return node.isWord

        
        return dfs(0, self.root)
        

