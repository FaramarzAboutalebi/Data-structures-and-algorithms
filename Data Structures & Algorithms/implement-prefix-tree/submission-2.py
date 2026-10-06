class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):

        self.trie = TrieNode()

    def insert(self, word: str) -> None:

        # time complexity: O(L)
        # space complexity: O(L)

        cur = self.trie

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


    def search(self, word: str) -> bool:

        # time complexity: O(L)
        # space complexity: O(1)

        cur = self.trie

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord
        
    def startsWith(self, prefix: str) -> bool:


        # time complexity: O(L)
        # space complexity: O(1)

        cur = self.trie

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True
        
        