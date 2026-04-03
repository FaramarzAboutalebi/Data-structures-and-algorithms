class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    ###    
    def insert(self, word: str)->None:
        # time complexity: O(n)
        # space complexity: O(k)
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    ###    
    def search(self, word: str)->bool:
        # time complexity: O(n)
        # space complexity: O(1)
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        
    ###
    def startsWith(self, word: str)->bool:
        # time complexity: O(n)
        # space complexity: O(1)
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
trie = PrefixTree()  
trie.insert("dog")
print(trie.search("dog"))
print(trie.search("do"))
print(trie.startsWith("do"))
trie.insert("do")
print(trie.search("do"))