class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:

        # time complexity: O(L)
        # space complexity: O(L)

        cur = self.trie
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
   

    def search(self, word: str) -> bool:
        
        # time complexity: 
            # without '.': O(L)
            # with '.' worst case : O(26^L)
        # space complexity: O(L)

        def dfs(i,node):
            for j in range(i,len(word)):

                c = word[j]

                if c == ".":
                    for child in node.children.values():
                        if dfs(j+1, child):
                            return True
                    return False

                if c not in node.children:
                    return False

                node = node.children[c]
            return node.isWord

        return dfs(0,self.trie)

# time complexity: 
# space complexity:






